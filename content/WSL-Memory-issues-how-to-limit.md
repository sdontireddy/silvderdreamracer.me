Title: Windows Subsystem for Linux(WSL)Memory Issues - How to Limit
Date: 2023-01-30 01:53
Author: sdontireddy
Category: OS
Tags: WSL, Windows11, Memory , vmmemWSL , WSL2
Slug: windows-wsl-memory-issues
Status: published


### Windows Subsystem for Linux (WSL2) Memory Usage - Limiting
According to Windows docs , 

```
The version of WSL that you are running will impact the configuration settings. WSL 2 runs as a lightweight virtual machine (VM), 
so uses virtualization settings that allow you to control the amount of memory or processors used (which may be familiar if you use Hyper-V or VirtualBox).
```

By Defautlt , 50% of total memory on Windows or 8GB, whichever is less; on builds before 20175: 80% of your total memory on Windows.

So default settings takes lot of  RAM.

#### Solution:

Create a new file <b>C:\Users\YourUsername\\.wslconfig</b> and set memory according to your needs.
Example 
```
[wsl2]
memory=3GB
```

Restart WSL

```
wsl --shutdown
```

YOu can run <b>free</b> from WSL terminal to check how much is allocated and how much is avaiable

Please refer to [here](https://learn.microsoft.com/en-us/windows/wsl/wsl-config#configuration-setting-for-wslconfig) for advanced settings
