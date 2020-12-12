# ssh
Scripts used to access the VM through ssh from the host OS.

## ssh_cred.txt

Stores the IP, username and password used to access to the VM. Note that the IP does not have to be the same one after rebooting the VM.

## ssh_login.sh

It reads the variables from "ssh_cred.txt" and it calls to "ssh_login_expect.sh" with the read values.

It acts as a wrapper for "ssh_login_expect.sh" for using the script through a predefined credentials file.

```
./ssh_login.sh
```

## ssh_login_expect.sh

Expect script which performs the ssh login into the windows VM. Once it has been login it access to the PowerShell and leave it open for the user.

Its usage is the following one.

```
./ssh_login_expect.sh <ip> <username> <password>
```
- ip
- username: It can have a space in between, such as "Fran Colmenar".
- password