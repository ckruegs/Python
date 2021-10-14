#!/usr/bin/env python3

import subprocess
import argparse
import re
from colorama import Fore, Back, Style

def get_arguments():
    # Create argument parser object
    parser = argparse.ArgumentParser()

    # Add arguments
    parser.add_argument('-i', '--interface', dest='interface', help='Interface for which to change MAC Address')
    parser.add_argument('-m', '--mac', dest='new_mac', help='New MAC Address')

    # Parse args and return (builds Namespace obj)
    options = parser.parse_args()

    # Handle exceptions
    if not options.interface:
        parser.error(f"{Fore.RED}[-] Please specify an interface, use '--help' for more info.")
    elif not options.new_mac:
        parser.error(f"{Fore.RED}[-] Please specify a MAC Address, use '--help' for more info.")

    return options

def change_mac(interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    # Grab 'ifconfig' result
    ifconfig_result = subprocess.check_output(["ifconfig", interface], encoding='utf8')

    # Use re to grab MAC Address from ifconfig results
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result) )

    if mac_address_search_result:
        return mac_address_search_result.group()
    else:
        print(f"{Fore.RED}[-] Could not read MAC Address.")

options = get_arguments()

current_mac = get_current_mac(options.interface)

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)

if current_mac == options.new_mac:
    print(f"{Fore.GREEN}[+] MAC Address for {options.interface} was successfully changed to {current_mac}")
else:
    print(f"{Fore.RED}[-] MAC Address was not changed.")