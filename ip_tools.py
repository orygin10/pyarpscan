# -*- coding: utf-8 -*-
"""IP address manipulations for my module pyarpscan
Functions:
calc_network
ask_for_ip
ask_for_netmask
"""
from ipaddress import IPv4Address, IPv4Network
import socket

def calc_network(ip_address, netmask):
    """Compute network address from an ip address and a netmask
    Args:
        ip_address (str): An IP address from the network
        netmask (str): The network mask

    Returns:
        IPv4Network: ipaddress module object for network

    Example:
        calc_network("192.168.1.54", "255.255.255.0")
        >>> IPv4Network("192.168.1.0/24")
    """
    return IPv4Network("%s/%s" % (ip_address, netmask), strict=False)

def ask_for_ip():
    """Ask user input for his IP address, otherwise use IP address provided by socket
    Returns:
        ip_found: IP address provided by socket
        IPv4Address(ip_input): User-input address, the function IPv4Address() is used
        to raise a ValueError exception if ip_input is not a valid IPv4 address.

    Note: ip_found is (str) type and IPv4Address(ip_input) is (IPv4Address) type,
    despite the difference, both return values can be used as string
    """
    ip_found = socket.gethostbyname(socket.gethostname())
    print("Ouvrez une invite de commandes Windows et entrez ipconfig")
    ip_input = input("Appuyez sur ENTRER si votre adresse IPv4 est %s, sinon ecrivez-la : "
                     % ip_found
                    )
    if ip_input == '':
        return ip_found
    else:
        try:
            return IPv4Address(ip_input)
        except ValueError:
            print("%s n'est pas une adresse IPv4 valide ..." % ip_input)
            raise SystemExit

def ask_for_netmask():
    """Ask user for his network mask, otherwise use default class C netmask
    Returns:
        netmask_default: Class C /24 netmask "255.255.255.0"
        IPv4Address(netmask_input): User-input netmask, the function IPv4Address() is used
        to raise a ValueError exception if netmask_input is not a valid IPv4 netmask/address
    TODO: use another method to check user-input netmask
    """
    netmask_default = "255.255.255.0"
    netmask_input = input("Appuyez sur ENTRER si votre masque de sous-réseau est %s, sinon ecrivez-le : "
                          % netmask_default
                         )
    if netmask_input == '':
        return netmask_default
    else:
        try:
            return IPv4Address(netmask_input)
        except ValueError:
            print("%s n'est pas un masque de sous-réseau valide ..." % netmask_input)
            raise SystemExit
