#!/usr/bin/expect -f

############################# Input Handling #############################

if { $argc == 3 } {  ###### No space at the username ######

  set ip [lindex $argv 0];  # Read the IP which is always the first value
  set username [lindex $argv 1];  # Username
  set password [lindex $argv 2];  # Password

} elseif { $argc == 4 } {  ###### Username with a space ######

  set ip [lindex $argv 0];  # IP
  set aux1 [lindex $argv 1]; # Username part 1
  set aux2 [lindex $argv 2]; # Username part 2
  set username "$aux1 $aux2";  # Username constructed from the parts
  set password [lindex $argv 3]; # Password

} else { ###### Wrong Format ######
  puts "Wrong number of arguments provided"
  puts "<ip> <username> <username_par_two_optional> <password>"
  exit 1
}

send "echo $ip\n"
send "echo $username\n"
send "echo $password\n"


