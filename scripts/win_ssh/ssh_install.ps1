# Check that SSH is not installed at windows
Get-WindowsCapability -Online | ? Name -like 'OpenSSH*'

# Install the OpenSSH Client
Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

# Install the OpenSSH Server
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0

# Enable the port 22 for SSH
netsh advfirewall firewall add rule name = "SSHD Port" dir = in action = allow protocol = TCP localport = 22

# Run SSH
& .\ssh_run.ps1

# TODO Add option to run them automatically on set up