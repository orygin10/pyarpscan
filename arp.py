# -*- coding: utf-8 -*-
"""Use windows-only libraries to send ARP who-has requests
Functions :
arp_exists
arp_host
"""
import ctypes
from ipaddress import IPv4Address

def arp_exists(host):
    """ Send ARP who-has request using Microsoft's Iphlpapi.lib
    Args:
        host (str): IP address to request
    Returns:
        True if IP address answers to ARP who-has, False otherwise

    DWORD SendARP(
    _In_    IPAddr DestIP,
    _In_    IPAddr SrcIP,
    _Out_   PULONG pMacAddr,
    _Inout_ PULONG PhyAddrLen
    );

    DestIP is decimal value of inverted IP address, for instance :
    10.0.0.103 => 103.0.0.10 => 1728053258
    Microsoft recommands wsock32.inet_addr(), which I can't use with Python 2.
    """

    SendARP = ctypes.windll.Iphlpapi.SendARP
    #inetaddr = ctypes.windll.wsock32.inet_addr(host) #Fonctionne uniquement sous Python 2
    inetaddr = int(IPv4Address('.'.join(host.split(".")[::-1])))

    buffer = ctypes.c_buffer(6)
    addlen = ctypes.c_ulong(ctypes.sizeof(buffer))

    if SendARP(inetaddr, 0, ctypes.byref(buffer), ctypes.byref(addlen)) == 0:
        return True
    return False

def arp_host(host):
    """Write IP address if host answers, otherwise do nothing
    Args:
        host (str): IP address to request
    """
    if arp_exists(host):
        print(host)
