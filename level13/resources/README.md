## 1 Disassembling the Main Function:

``` bash
level13@SnowCrash:~$ gdb

(gdb) disas main
```

This command disassembles the main function, showing the assembly code. It reveals the flow of execution, including calls to getuid and comparisons with expected UID values.

## 2 Setting a Breakpoint:

``` bash 
(gdb) break getuid
```
Set a breakpoint at the getuid function, so the debugger will pause execution whenever getuid is called. This allows you to inspect or modify the returned value.

## 3 Running the Program:

``` bash 
(gdb) run
``` 

This starts the execution of the level13 program. The program will execute until it hits the breakpoint set at getuid.
## 4 Hit the Breakpoint:

``` bash 
Breakpoint 1, 0xb7ee4cc0 in getuid () from /lib/i386-linux-gnu/libc.so.6
```

Execution stops at the getuid function. You are now in a position to inspect and manipulate the return value.

## 6 Stepping Through the Code:
``` bash 
(gdb) step
```
Step through the code line by line, moving to the next instruction to observe how the program behaves.

## 7 Inspecting the Register:

``` bash 
(gdb) print $eax
``` 
Print the value of the eax register, which stores the return value of getuid. 

Initially, it shows your actual UID, which is 2013.
## 7 Modifying the Return Value:

``` bash 
(gdb) set $eax=4242
``` 
Here, set the eax register to 4242, which is the expected UID that the program checks for. This modification allows the program to think it has the required UID.
## 8 Continue Execution:

``` bash 
(gdb) step
``` 
After modifying the UID, you continue stepping through the program. Eventually, the execution continues to the part where the token is printed.
Output the Token:

``` bash 
your token is 2A31L79asukciNyi8uppkEuSx
```

At this point, the program successfully prints the token since it passed the UID check.

## 9 Exiting GDB:

``` bash 
(gdb) quit
```
Finally,  quit GDB. It prompts to confirm the exit, and  choose to exit, terminating the debugging session.

Aimed to bypass a UID check by manipulating the return value of getuid in the level13 executable.
Technique: Using GDB, you set a breakpoint at getuid, modified the return value directly in the register, and continued the program to get the token required to advance to the next level.

## 10 Enter level 14

su level14
Password: 2A31L79asukciNyi8uppkEuSx