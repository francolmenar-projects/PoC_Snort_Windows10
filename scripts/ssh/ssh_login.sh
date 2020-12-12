#!/usr/bin/env bash

. ssh_cred.txt # Read the values to be used for the ssh log in

./ssh_login_expect.sh $ip $username $psw

# Install vim
# choco install vim -y

# Create folder
#  New-Item -Path "C:\Users\Fran Colmenar\scripts" -ItemType Directory
# New-Item -Path C:\Users\'Fran Colmenar' -Name "scr2.ps1" -Value "Write-Host 'Congratulations! Your first script executed successfully'"

