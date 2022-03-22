#!/usr/bin/env python3

import subprocess, optparse, re

# Get user arguments for interface and MAC
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    #initialize options and arguments with what is returned from parser.parse_args()
    (options, arguments) = parser.parse_args()

    if not options.interface:
        # error handling
        parser.error("[-] Please specify an interface, use '--help' for more info.")
    elif not options.new_mac:
        # error handling
        parser.error("[-] Please specify a new MAC address, use '--help' for more info.")
    return options
# Function to handle system calls to change mac
def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode('utf-8')
    # MAC address regex
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group()
    else:
        print("[-] Could not read MAC address.")

# map user defined arguments
options = get_arguments()

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print(f"[+] MAC address was successfully changed to {current_mac}.")
else:
    print(f"[-] MAC address was not changed.")

change_mac(options.interface, options.new_mac)