# Given an IP address as input, write a Python program to check whether the given IP
# Address is Valid or not.
# Input:  192.168.0.1
# Output: Valid Ip address
#
# Input: 110.234.52.124
# Output: Valid Ip address
#
# Input: 666.1.2.2
# Output: Invalid Ip addess

import re

regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''

def valid_ip_address(ip_str):

    if re.search(regex, ip_str):
        print("Valid!")
    else:
        print("Invalid!")

ip_str = "192.168.0.1"
valid_ip_address(ip_str)