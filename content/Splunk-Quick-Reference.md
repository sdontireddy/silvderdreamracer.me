Title: Splunk Query Reference guide
Date: 2021-06-21 01:53
Author: sdontireddy
Category: Splunk
Tags: Splunk, Reference , Cheat Sheet
Slug: splunk-query-reference-guide
Status: published


**Simple Search with various AND**
index=index_name sourcetype=source_type  host=host_nam source=source

**Count of search criteria "LifecycleException" per day**
index=index_name sourcetype=exception_source_typs host=host_name LifecycleException | bucket _time span=day |stats count by _time

**Count of search criteria "LifecycleException" by app**
index=index_name sourcetype=exception_source_typs host=host_name LifecycleException | stats count by originApplication

**Dedup : Remove duplicates by Time**
index=index_name sourcetype=exception_source_typs host=host_name  "java.lang.OutOfMemoryError" | sort - _time desc |table host,_time,source |  bin _time span=300sec | dedup _time


**Display Detailed Information on All Fields Available Within a Search**

your_search_criteria | fieldsummary


**Time Stamp**

|  eval Date=strftime(_time, "%Y-%m-%d")`

**Convert _time to a date in the needed forma**

search | convert timeformat="%Y-%m-%d" ctime(_time) AS date | stats count by date


**OutOfMemory Search** 
index=INDEX_NAME host=HOST_NAME  "java.lang.OutOfMemoryError" | sort - _time desc |table host,_time |  bin _time span=300sec | dedup _time 

**Extract MultiValue field from a File**
 search inv_sync_file=*FILE_NAME.XML*  | eval Date=strftime(_time, "%+") , File = inv_sync_file|
rex max_match=0 field=_raw "VendorPartNumber\": \"(?<VendorNum>\w*)\"" | mvexpand VendorNum | table VendorNum

**Condition**

search your_search_with Valid as a field|| eval var=if(Valid  > 10, "false", "true") 


**Add the column and show as report**
Ex: |table Date , _time,  File, Valid, Invalid|addcoltotals  | sort - _time desc


**Adds all the columns in a search results and displays another column**

addtotals fieldname=sum
Ex: |table Date , _time,  File, Valid, Invalid|addtotals fieldname=sum 

## Dashboards 
**How to add labels to Dashboard**
```
<html>
<h5>…text</h5>
</html>
```

**Splunk regex by default searches single line , to make regex for multiline (?m) and to match all the results matching regex**
your_search_criteria  | rex max_match=0 field=_raw "(?m)\n(?<message>.*)" | table message,_raw 

**Search for a Word using regular expression and retrieving fields on** 
your_search_criteria  | eval responseXML=replace(_raw,"^([\S\s\r\n]*)WORD_TOBE_SEARCHED","")|  spath input=responseXML path=XXXX{}.YYY output=filed_output | table filed_output


**Charts OverLay**

your_search_criteria  ConcurrentModificationException| timechart count as Exceptions_Count span=1h useother=f  |appendcols  [search another_search_criteria | timechart count as sub_count span=1h]

**SPAPTH with XML namespace**

your_search_criteria |eval xmessagePayload = messagePayload |  spath input=xmessagePayload output=xorderID path=ord:AddOrderV2.ord:order.ff:AltOrderID  |stats count(xorderID)

**Get list of dest_ip which are not common between Yesterday and Today**

your_search_criteria| set diff [search sourcetype=nessus source=*Host_Enumeration* earliest=-3d@d latest=-2d@d | stats count by dest_ip |table dest_ip] [search sourcetype=nessus source=*Host_Enumeration* earliest=-1d@d latest=now | stats count by dest_ip |table dest_ip]
