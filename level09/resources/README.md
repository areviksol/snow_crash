## 1 Directory Contents`

When you access the directory, you will find the following files:
``` bash
level09@SnowCrash:~$ ls
level09  token
```
* Token File

The token file contains a binary representation of a string that has been encrypted.

Output from cat token
When you view the contents of the token file, you will see something like this:
``` bash 
level09@SnowCrash:~$ cat token
f4kmm6p|=?p?n??DB?Du{??
```
## 2  Executing the Level Binary

To decrypt the token, execute the binary with the following command:

``` bash
level09@SnowCrash:~$ ./level09 token 
tpmhr
```

Understanding the Binary Data
When you check the token file type using:

``` bash
level09@SnowCrash:~$ file token 
token: data
```

Binary Data Explanation
Data: Indicates that the file contains raw binary information rather than structured text.
Non-Text Content: The content might include non-printable characters, special symbols, or a mix of formats that do not conform to standard text encodings.
Verifying Binary Data
To further verify the contents of the token file, you can use hexdump:

``` bash
level09@SnowCrash:~$ file token 
token: data
level09@SnowCrash:~$ hexdump -C token
00000000  66 34 6b 6d 6d 36 70 7c  3d 82 7f 70 82 6e 83 82  |f4kmm6p|=..p.n..|
00000010  44 42 83 44 75 7b 7f 8c  89 0a                    |DB.Du{....|
0000001a
```

This command provides a hexadecimal representation of the binary data along with its ASCII equivalents.

## 3 Encryption 
The encryption process modifies each character in the plaintext by adding its index to the ASCII value:

``` python
for i in range(len(plaintext)):
    ch = plaintext[i]
    n = i  # n is the index
    encrypted_char = chr(ord(ch) + n)
Decryption Logic
To reverse the encryption process, you subtract the index from the ASCII value of each character in the token. This is implemented in the decrypt.py script:

token = [0x66, 0x34, 0x6b, 0x6d, 0x6d, 0x36, 0x70, 0x7c,
         0x3d, 0x82, 0x7f, 0x70, 0x82, 0x6e, 0x83, 0x82,
         0x44, 0x42, 0x83, 0x44, 0x75, 0x7b, 0x7f, 0x8c, 0x89]

reverse_hash = ""

# Reverse the transformation
for i in range(len(token)):
    token[i] -= i  # Subtract the index from the byte value
    if token[i] < 0:  # If the result is negative
        token[i] += 127  # Wrap around by adding 127
    reverse_hash += chr(token[i])  # Convert to character and build the result

print(reverse_hash)  # Output the reversed string
```
Obtaining the Password
After decrypting the token, you will obtain the password required for the next level:

## 4 Enter level10

``` bash
level09@SnowCrash:~$ su flag09
Password: f3iji1ju5yuevaus41q1afiuq
Don't forget to launch getflag !
flag09@SnowCrash:~$ getflag
Check flag.Here is your token : s5cAJpM8ev6XHw998pRWG728z
flag09@SnowCrash:~$ su level10
Password: s5cAJpM8ev6XHw998pRWG728z
```