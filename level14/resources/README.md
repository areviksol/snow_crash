level14@SnowCrash:~$ ls
level14@SnowCrash:~$ gdb /bin/getflag 
GNU gdb (Ubuntu/Linaro 7.4-2012.04-0ubuntu2.1) 7.4-2012.04
Copyright (C) 2012 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "i686-linux-gnu".
For bug reporting instructions, please see:
<http://bugs.launchpad.net/gdb-linaro/>...
Reading symbols from /bin/getflag...(no debugging symbols found)...done.
(gdb) disas main 
Dump of assembler code for function main:
______
   0x08048dea <+1188>:	mov    %eax,%ebx
   0x08048dec <+1190>:	movl   $0x8049220,(%esp)
   0x08048df3 <+1197>:	call   0x8048604 <ft_des>
   0x08048df8 <+1202>:	mov    %ebx,0x4(%esp)
   0x08048dfc <+1206>:	mov    %eax,(%esp)
   0x08048dff <+1209>:	call   0x8048530 <fputs@plt>
   0x08048e04 <+1214>:	jmp    0x8048e2f <main+1257>
   0x08048e06 <+1216>:	mov    0x804b060,%eax
   0x08048e0b <+1221>:	mov    %eax,%edx
   0x08048e0d <+1223>:	mov    $0x8049248,%eax
   0x08048e12 <+1228>:	mov    %edx,0xc(%esp)
   0x08048e16 <+1232>:	movl   $0x38,0x8(%esp)
   0x08048e1e <+1240>:	movl   $0x1,0x4(%esp)
   0x08048e26 <+1248>:	mov    %eax,(%esp)
   0x08048e29 <+1251>:	call   0x80484c0 <fwrite@plt>
   0x08048e2e <+1256>:	nop
   0x08048e2f <+1257>:	mov    0x804b060,%eax
   0x08048e34 <+1262>:	mov    %eax,0x4(%esp)
   0x08048e38 <+1266>:	movl   $0xa,(%esp)
   0x08048e3f <+1273>:	call   0x8048520 <fputc@plt>
   0x08048e44 <+1278>:	jmp    0x8048ead <main+1383>
   0x08048e46 <+1280>:	movl   $0x8049281,0x4(%esp)
   0x08048e4e <+1288>:	lea    0x1c(%esp),%eax
---Type <return> to continue, or q <return> to quit---
   0x08048e52 <+1292>:	mov    %eax,(%esp)
   0x08048e55 <+1295>:	call   0x80487be <afterSubstr>
   0x08048e5a <+1300>:	test   %eax,%eax
   0x08048e5c <+1302>:	jne    0x8048e89 <main+1347>
   0x08048e5e <+1304>:	mov    0x804b040,%eax
   0x08048e63 <+1309>:	mov    %eax,%edx
   0x08048e65 <+1311>:	mov    $0x8049294,%eax
   0x08048e6a <+1316>:	mov    %edx,0xc(%esp)
   0x08048e6e <+1320>:	movl   $0x30,0x8(%esp)
   0x08048e76 <+1328>:	movl   $0x1,0x4(%esp)
   0x08048e7e <+1336>:	mov    %eax,(%esp)
   0x08048e81 <+1339>:	call   0x80484c0 <fwrite@plt>
   0x08048e86 <+1344>:	jmp    0x8048ead <main+1383>
   0x08048e88 <+1346>:	nop
   0x08048e89 <+1347>:	mov    0x14(%esp),%eax
   0x08048e8d <+1351>:	mov    %eax,0x8(%esp)
   0x08048e91 <+1355>:	movl   $0x100,0x4(%esp)
   0x08048e99 <+1363>:	lea    0x1c(%esp),%eax
   0x08048e9d <+1367>:	mov    %eax,(%esp)
   0x08048ea0 <+1370>:	call   0x804874c <syscall_gets>
   0x08048ea5 <+1375>:	test   %eax,%eax
   0x08048ea7 <+1377>:	jne    0x8048a89 <main+323>
   0x08048ead <+1383>:	mov    $0x0,%eax
---Type <return> to continue, or q <return> to quit---
   0x08048eb2 <+1388>:	mov    0x11c(%esp),%edx
   0x08048eb9 <+1395>:	xor    %gs:0x14,%edx
   0x08048ec0 <+1402>:	je     0x8048ec7 <main+1409>
   0x08048ec2 <+1404>:	call   0x80484a0 <__stack_chk_fail@plt>
   0x08048ec7 <+1409>:	mov    -0x4(%ebp),%ebx
   0x08048eca <+1412>:	leave  
   0x08048ecb <+1413>:	ret    
End of assembler dump.
(gdb) 
(gdb) b main 
Breakpoint 1 at 0x804894a
(gdb) jump *v
The program is not being run.
(gdb) jump *0x08048de5
The program is not being run.
(gdb) r
Starting program: /bin/getflag 

Breakpoint 1, 0x0804894a in main ()
(gdb) jump *0x08048de5
Continuing at 0x8048de5.
7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ
*** stack smashing detected ***: /bin/getflag terminated
======= Backtrace: =========
/lib/i386-linux-gnu/libc.so.6(__fortify_fail+0x45)[0xb7f2fd95]
/lib/i386-linux-gnu/libc.so.6(+0x103d4a)[0xb7f2fd4a]
/bin/getflag[0x8048ec7]
/lib/i386-linux-gnu/libc.so.6(__libc_start_main+0xf3)[0xb7e454d3]
/bin/getflag[0x8048571]
======= Memory map: ========
08048000-0804a000 r-xp 00000000 07:00 12700      /bin/getflag
0804a000-0804b000 r--p 00001000 07:00 12700      /bin/getflag
0804b000-0804c000 rw-p 00002000 07:00 12700      /bin/getflag
0804c000-0806d000 rw-p 00000000 00:00 0          [heap]
b7e07000-b7e23000 r-xp 00000000 07:00 14117      /lib/i386-linux-gnu/libgcc_s.so.1
b7e23000-b7e24000 r--p 0001b000 07:00 14117      /lib/i386-linux-gnu/libgcc_s.so.1
b7e24000-b7e25000 rw-p 0001c000 07:00 14117      /lib/i386-linux-gnu/libgcc_s.so.1
b7e2b000-b7e2c000 rw-p 00000000 00:00 0 
b7e2c000-b7fcf000 r-xp 00000000 07:00 14123      /lib/i386-linux-gnu/libc-2.15.so
b7fcf000-b7fd1000 r--p 001a3000 07:00 14123      /lib/i386-linux-gnu/libc-2.15.so
b7fd1000-b7fd2000 rw-p 001a5000 07:00 14123      /lib/i386-linux-gnu/libc-2.15.so
b7fd2000-b7fd5000 rw-p 00000000 00:00 0 
b7fd9000-b7fdd000 rw-p 00000000 00:00 0 
b7fdd000-b7fde000 r-xp 00000000 00:00 0          [vdso]
b7fde000-b7ffe000 r-xp 00000000 07:00 14081      /lib/i386-linux-gnu/ld-2.15.so
b7ffe000-b7fff000 r--p 0001f000 07:00 14081      /lib/i386-linux-gnu/ld-2.15.so
b7fff000-b8000000 rw-p 00020000 07:00 14081      /lib/i386-linux-gnu/ld-2.15.so
bffdf000-c0000000 rw-p 00000000 00:00 0          [stack]
