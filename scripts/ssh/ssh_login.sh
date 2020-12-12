#!/usr/bin/env bash

.  credential.txt  # Read the values to be used for the ssh log in

./ssh_login_expect.sh $ip $username $psw 


