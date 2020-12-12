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
  puts "Wrong number of arguments provided";
  puts "<ip> <username> <username_par_two_optional> <password>";
  exit 1;
}

############################# SSH Connection #############################

set prompt "C:\Users\$username>";  # Set the promts using the username provided
set ps_prompt "PS C:\Users\$username>";

spawn ssh $username@$ip;  # SSH Connection

expect "password:";  # Send the password
send "$password\r";

expect "$prompt";  # cmd prompt to PS
send "powershell\r";

expect "$ps_prompt"; # PS prompt
send "dir\r";

interact


