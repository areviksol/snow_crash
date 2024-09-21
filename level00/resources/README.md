Level 00 Challenge - SnowCrash

Objective

The goal of this challenge is to escalate privileges and retrieve a flag from the system.

Steps Taken

## 1. Finding User Files

First, we searched for files owned by the user `flag00`:
```console
level00@SnowCrash:~$ find / -user flag00 2>/dev/null
/usr/sbin/john
/rofs/usr/sbin/john
```

## 2. Viewing the File Contents

We examined the contents of the `/rofs/usr/sbin/john` file:
```console
level00@SnowCrash:~$ cat /rofs/usr/sbin/john
cdiiddwpgswtgt
```

This same content was found in `/usr/sbin/john`:
```console
level00@SnowCrash:~$ cat /usr/sbin/john
cdiiddwpgswtgt
```

## 3. Connecting via SSH

Next, we established an SSH connection to the local host:

```console
level00@SnowCrash:~$ ssh arev@localhost -p 4243
```
## 4. Gaining Root Access

Once connected, we switched to the root user:

```console
# arev@debian:~$ su root
Password: 
```
## 5. Installing Required Packages

We updated the package lists and installed Python 3 along with pip and venv:

```console
root@debian:/home/arev# apt update
root@debian:/home/arev# apt install python3 python3-pip python3-venv
```

## 6. Creating the Decrypt Script

We created a Python script named `caesar_decrypt.py` to decrypt the encoded string:

```console
root@debian:/home/arev# vim caesar_decrypt.py 
```

Decrypting the String

We ran the script to try different shifts and found the following output:

```console
python3 caesar_decrypt.py           
Shift 0: cdiiddwpgswtgt
Shift 1: bchhccvofrvsfs
Shift 2: abggbbunequrer
Shift 3: zaffaatmdptqdq
Shift 4: yzeezzslcospcp
Shift 5: xyddyyrkbnrobo
Shift 6: wxccxxqjamqnan
Shift 7: vwbbwwpizlpmzm
Shift 8: uvaavvohykolyl
Shift 9: tuzzuungxjnkxk
Shift 10: styyttmfwimjwj
Shift 11: rsxxsslevhlivi
Shift 12: qrwwrrkdugkhuh
Shift 13: pqvvqqjctfjgtg
Shift 14: opuuppibseifsf
Shift 15: nottoohardhere
Shift 16: mnssnngzqcgdqd
Shift 17: lmrrmmfypbfcpc
Shift 18: klqqllexoaebob
Shift 19: jkppkkdwnzdana
Shift 20: ijoojjcvmyczmz
Shift 21: hinniibulxbyly
Shift 22: ghmmhhatkwaxkx
Shift 23: fgllggzsjvzwjw
Shift 24: efkkffyriuyviv
Shift 25: dejjeexqhtxuhu
```

## 7. Switching to `flag00` User

Using the decrypted password, we switched to the `flag00` user:

```console
level00@SnowCrash:~$ su flag00
Password: nottoohardhere
```
## 8. Retrieving the Flag

Finally, we executed the `getflag` command to obtain the flag:

```console
flag00@SnowCrash:~$ getflag
Check flag. Here is your token: x24ti5gi3x0ol2eh4esiuxias
```
## 9. Progressing to Level 01

We then switched to the `level01` user using the retrieved token as the password:

```console
level00@SnowCrash:~$ su level01
Password: x24ti5gi3x0ol2eh4esiuxias 
```
