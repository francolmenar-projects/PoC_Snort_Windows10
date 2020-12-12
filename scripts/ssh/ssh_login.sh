#!/usr/bin/env bash

. ssh_cred.txt # Read the values to be used for the ssh login

./ssh_login_expect.sh $ip $username $psw
