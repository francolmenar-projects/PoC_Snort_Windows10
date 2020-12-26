# syn_flood
Basic python file used to simulate a Syn Flood Attack using scapy. 

It is based on the project [pyddos](https://github.com/mach1el/pyddos) by [mach1el](https://github.com/mach1el).

 - **main**: CLI entry point to choose which attack to be used. It is easily modified to include further attacks.
 
```
sudo python main.py run -atk syn -d 127.0.0.1 -p 80 -s 127.0.0.1 -t 50

sudo python main.py -atk <attack to be used> -d <ip> -p <port> -s <source address> -t <number of threads>
```
  
  - **syn_flood**: File performing a SYN Flood Attack. 
 
```
sudo python syn_flood.py -d 127.0.0.1 -p 80 -s 127.0.0.1 -t 50

sudo python syn_flood.py -d <ip> -p <port> -s <source address> -t <number of threads>
```
 
