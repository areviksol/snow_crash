## 1. Checking User Accounts
To view the list of user accounts and their associated password hashes, you can use the getent passwd command.

``` console
level01@SnowCrash:~$ getent passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/bin/sh
bin:x:2:2:bin:/bin:/bin/sh
sys:x:3:3:sys:/dev:/bin/sh
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/bin/sh
man:x:6:12:man:/var/cache/man:/bin/sh
lp:x:7:7:lp:/var/spool/lpd:/bin/sh
mail:x:8:8:mail:/var/mail:/bin/sh
news:x:9:9:news:/var/spool/news:/bin/sh
uucp:x:10:10:uucp:/var/spool/uucp:/bin/sh
proxy:x:13:13:proxy:/bin:/bin/sh
www-data:x:33:33:www-data:/var/www:/bin/sh
backup:x:34:34:backup:/var/backups:/bin/sh
list:x:38:38:Mailing List Manager:/var/list:/bin/sh
irc:x:39:39:ircd:/var/run/ircd:/bin/sh
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/bin/sh
nobody:x:65534:65534:nobody:/nonexistent:/bin/sh
libuuid:x:100:101::/var/lib/libuuid:/bin/sh
syslog:x:101:103::/home/syslog:/bin/false
messagebus:x:102:106::/var/run/dbus:/bin/false
whoopsie:x:103:107::/nonexistent:/bin/false
landscape:x:104:110::/var/lib/landscape:/bin/false
sshd:x:105:65534::/var/run/sshd:/usr/sbin/nologin
level00:x:2000:2000::/home/user/level00:/bin/bash
level01:x:2001:2001::/home/user/level01:/bin/bash
level02:x:2002:2002::/home/user/level02:/bin/bash
level03:x:2003:2003::/home/user/level03:/bin/bash
level04:x:2004:2004::/home/user/level04:/bin/bash
level05:x:2005:2005::/home/user/level05:/bin/bash
level06:x:2006:2006::/home/user/level06:/bin/bash
level07:x:2007:2007::/home/user/level07:/bin/bash
level08:x:2008:2008::/home/user/level08:/bin/bash
level09:x:2009:2009::/home/user/level09:/bin/bash
level10:x:2010:2010::/home/user/level10:/bin/bash
level11:x:2011:2011::/home/user/level11:/bin/bash
level12:x:2012:2012::/home/user/level12:/bin/bash
level13:x:2013:2013::/home/user/level13:/bin/bash
level14:x:2014:2014::/home/user/level14:/bin/bash
flag00:x:3000:3000::/home/flag/flag00:/bin/bash
flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash
flag02:x:3002:3002::/home/flag/flag02:/bin/bash
flag03:x:3003:3003::/home/flag/flag03:/bin/bash
flag04:x:3004:3004::/home/flag/flag04:/bin/bash
flag05:x:3005:3005::/home/flag/flag05:/bin/bash
flag06:x:3006:3006::/home/flag/flag06:/bin/bash
flag07:x:3007:3007::/home/flag/flag07:/bin/bash
flag08:x:3008:3008::/home/flag/flag08:/bin/bash
flag09:x:3009:3009::/home/flag/flag09:/bin/bash
flag10:x:3010:3010::/home/flag/flag10:/bin/bash
flag11:x:3011:3011::/home/flag/flag11:/bin/bash
flag12:x:3012:3012::/home/flag/flag12:/bin/bash
flag13:x:3013:3013::/home/flag/flag13:/bin/bash
flag14:x:3014:3014::/home/flag/flag14:/bin/bash
```

This command retrieves the password database entries, displaying usernames and their hashed passwords.
## 2. Identifying the Target Hash
In the output of the getent command, locate the desired user account's password hash. For example, the user flag01 has the following entry:
``` console
flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash
```
The hash for flag01 is 42hDRfypTqqnw.

## 3. Creating a Password File
To prepare for password cracking, create a file that contains the hash you identified:
``` console
root@debian:/home/arev# echo '42hDRfypTqqnw' > password.txt 
```
## 4. Installing John the Ripper
If John the Ripper is not already installed, you can install it using apt:
``` console
root@debian:/home/arev# apt install john
```
Check the installation of John the Ripper to ensure it is accessible:
``` console
root@debian:~# dpkg -L john | grep bin
/usr/sbin
/usr/sbin/john
/usr/sbin/mailer
/usr/sbin/unafs
/usr/sbin/unique
/usr/sbin/unshadow
```
To run John easily, add its binary directory to your system's PATH:

``` console
root@debian:/home/arev# export PATH=$PATH:/usr/sbin
```

## 5. Cracking the Password
Now, you can use John the Ripper to attempt to crack the password using the hash file you create

``` console
root@debian:/home/arev# john --show password.txt 
?:abcdefg

1 password hash cracked, 0 left
```

If successful, John will output the cracked password, which you can use to log in.
## 6. Switching Users
Once you have the cracked password, you can switch to the flag01 user:
``` console
level01@SnowCrash:~$ su flag01
Password: abcdefg
Don't forget to launch getflag !
```
## 7 Retrieving the Flag
After switching users, you can retrieve the flag using the following command:
``` console
flag01@SnowCrash:~$ getflag
Check flag.Here is your token : f2av5il02puano7naaf6adaaf
```
This command will output your token, which serves as proof of successfully obtaining the flag.

## 8. Further Privilege Escalation
With the token obtained, you can use it to switch to the next user level:
``` console
flag01@SnowCrash:~$ su level02
Password: f2av5il02puano7naaf6adaaf
```
