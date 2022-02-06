
Title:  NRQL, New Relic's query language Quick Reference Guide
Date: 2022-05-02 21:53
Author: sdontireddy
Category: Observability
Tags: NewRelic , NRQL
Slug: NewRelic-Query-language-quick-reference-guide-NRQL
Status: published

# NewRelic NRQL Quick Reference Guide


**Select results in the given time of the hours**
SELECT hourof(timestamp)   FROM Transaction WHERE your_where_cluase and hourof(timestamp) in ('01:00','02:00','03:00','04:00','05:00','06:00','07:00','08:00') SINCE this week 


**Select results in the given time stamp range**
SELECT *  FROM Transaction WHERE your_search_query  SINCE '2020-07-06 20:00:00 EST' UNTIL '2020-07-06 22:23:00 EST'


**Average CPU**

SELECT average(memoryUsedBytes/memoryTotalBytes*100) FROM SystemSample TIMESERIES FACET `entityName` WHERE `entityName` IN ('HOST_NAME2','HOST_NAME2','HOST_NAME3') LIMIT 100 SINCE 60 minutes ago

**Diskspace**

SELECT average(diskUsedPercent) FROM StorageSample TIMESERIES FACET `entityName` WHERE `entityName` LIKE '%HOST_NAME%' LIMIT 100 SINCE 60 minutes

**Health**

SELECT min(status) FROM NetworkPortSample WHERE address LIKE 'HOST_NAME%' facet address TIMESERIES 1 hour SINCE yesterday UNTIL today


**RabbiMQ New Relic Plugin**

SELECT average(queue.totalMessages) FROM RabbitmqQueueSample WHERE entityName = 'queue:/your_queue_name' AND label.env = 'ENVIRONMENT' FACET clusterName TIMESERIES 1 minute SINCE '2020-04-23 22:51:00' UNTIL '2020-04-24 04:50:00'

**NewRelic Directory Watcher List of all files that are being monitored**
SELECT timestamp ,`dir.oldest.name` AS Name ,`dir.oldest.last_modified` AS LastModfiedTime ,`dir.parent` AS PATH FROM DirWatcher where `dir.oldest.name` IS NOT NULL AND `dir.oldest.name` NOT IN ('$Log.txt','.DS_Store','._.DS_Store','NFLPA') LIMIT 1000

**Directory Watcher List of directories or mount locations being monitored**
SELECT uniqueCount(`dir.oldest.name`) FROM DirWatcher where `dir.parent` LIKE '%/mnt/your_Mount_location/%' AND `dir.oldest.name` IS NOT NULL AND `dir.oldest.name` NOT IN ('$Log.txt','.DS_Store','._.DS_Store','NFLPA') SINCE last hour FACET `dir.parent`

**Directory Watcher Comparision of number files in a given directories today compared to last week same day**

SELECT uniqueCount(`dir.newest.fullpath`) FROM DirWatcher SINCE 24 HOURS AGO COMPARE WITH 1 week AGO WHERE `dir.parent` = 'YOUR_DIRECTORY_BEING_MONITORED' AND `dir.newest.fullpath` IS NOT NULL TIMESERIES

**Errors - Top 5 by appID**
SELECT count(*) FROM TransactionError FACET `error.class`   TIMESERIES  WHERE appId = YOUR_APP_ID AND `error.expected` IS false SINCE 363 MINUTES AGO UNTIL 3 MINUTES AGO
