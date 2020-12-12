# Remove the OpenSSH Client
Remove-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

# Remove the OpenSSH Server
Remove-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0

# Stoping the service
Stop-Service sshd

# Check that SSH is removed at windows
Get-WindowsCapability -Online | ? Name -like 'OpenSSH*'
