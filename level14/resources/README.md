# Level 14 - Snow Crash

## Goal

Obtain the final token by bypassing the normal execution flow of `/bin/getflag` with `gdb`.

## Idea

The `getflag` binary contains a code path that prints the token after a call to `ft_des`.  
Instead of satisfying all normal checks, we jump directly to the instruction range that performs the output.

## Step-by-Step Walkthrough

### 1) Open the binary in GDB

```bash
level14@SnowCrash:~$ gdb /bin/getflag
```

### 2) Inspect `main`

```bash
(gdb) disassemble main
```

Full assembler excerpt used during the analysis:

```asm
Dump of assembler code for function main:
   0x08048dea <+1188>: mov    %eax,%ebx
   0x08048dec <+1190>: movl   $0x8049220,(%esp)
   0x08048df3 <+1197>: call   0x8048604 <ft_des>
   0x08048df8 <+1202>: mov    %ebx,0x4(%esp)
   0x08048dfc <+1206>: mov    %eax,(%esp)
   0x08048dff <+1209>: call   0x8048530 <fputs@plt>
   0x08048e04 <+1214>: jmp    0x8048e2f <main+1257>
   0x08048e06 <+1216>: mov    0x804b060,%eax
   0x08048e0b <+1221>: mov    %eax,%edx
   0x08048e0d <+1223>: mov    $0x8049248,%eax
   0x08048e12 <+1228>: mov    %edx,0xc(%esp)
   0x08048e16 <+1232>: movl   $0x38,0x8(%esp)
   0x08048e1e <+1240>: movl   $0x1,0x4(%esp)
   0x08048e26 <+1248>: mov    %eax,(%esp)
   0x08048e29 <+1251>: call   0x80484c0 <fwrite@plt>
   0x08048e2e <+1256>: nop
   0x08048e2f <+1257>: mov    0x804b060,%eax
   0x08048e34 <+1262>: mov    %eax,0x4(%esp)
   0x08048e38 <+1266>: movl   $0xa,(%esp)
   0x08048e3f <+1273>: call   0x8048520 <fputc@plt>
   0x08048e44 <+1278>: jmp    0x8048ead <main+1383>
   0x08048e46 <+1280>: movl   $0x8049281,0x4(%esp)
   0x08048e4e <+1288>: lea    0x1c(%esp),%eax
   0x08048e52 <+1292>: mov    %eax,(%esp)
   0x08048e55 <+1295>: call   0x80487be <afterSubstr>
   0x08048e5a <+1300>: test   %eax,%eax
   0x08048e5c <+1302>: jne    0x8048e89 <main+1347>
   0x08048e5e <+1304>: mov    0x804b040,%eax
   0x08048e63 <+1309>: mov    %eax,%edx
   0x08048e65 <+1311>: mov    $0x8049294,%eax
   0x08048e6a <+1316>: mov    %edx,0xc(%esp)
   0x08048e6e <+1320>: movl   $0x30,0x8(%esp)
   0x08048e76 <+1328>: movl   $0x1,0x4(%esp)
   0x08048e7e <+1336>: mov    %eax,(%esp)
   0x08048e81 <+1339>: call   0x80484c0 <fwrite@plt>
   0x08048e86 <+1344>: jmp    0x8048ead <main+1383>
   0x08048e88 <+1346>: nop
   0x08048e89 <+1347>: mov    0x14(%esp),%eax
   0x08048e8d <+1351>: mov    %eax,0x8(%esp)
   0x08048e91 <+1355>: movl   $0x100,0x4(%esp)
   0x08048e99 <+1363>: lea    0x1c(%esp),%eax
   0x08048e9d <+1367>: mov    %eax,(%esp)
   0x08048ea0 <+1370>: call   0x804874c <syscall_gets>
   0x08048ea5 <+1375>: test   %eax,%eax
   0x08048ea7 <+1377>: jne    0x8048a89 <main+323>
   0x08048ead <+1383>: mov    $0x0,%eax
   0x08048eb2 <+1388>: mov    0x11c(%esp),%edx
   0x08048eb9 <+1395>: xor    %gs:0x14,%edx
   0x08048ec0 <+1402>: je     0x8048ec7 <main+1409>
   0x08048ec2 <+1404>: call   0x80484a0 <__stack_chk_fail@plt>
   0x08048ec7 <+1409>: mov    -0x4(%ebp),%ebx
   0x08048eca <+1412>: leave
   0x08048ecb <+1413>: ret
End of assembler dump.
```

Look for the block around:

```asm
0x08048dea <+1188>: mov    %eax,%ebx
0x08048dec <+1190>: movl   $0x8049220,(%esp)
0x08048df3 <+1197>: call   0x8048604 <ft_des>
0x08048dff <+1209>: call   0x8048530 <fputs@plt>
```

This area is interesting because it decrypts and prints data.

### 3) Set a breakpoint on `main`

```bash
(gdb) break main
```

### 4) Run the program

```bash
(gdb) run
```

Execution stops at `main`.

### 5) Jump directly to the target address

```bash
(gdb) jump *0x08048de5
```

After continuing from this point, `getflag` prints the token string.

## Result

The token printed is:

```text
7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ
```

You may then see a stack-smashing message, which is expected in this shortcut path.  
The important part is that the token is already displayed.

## Next Step

Use this token to switch to the next account in the challenge flow.
