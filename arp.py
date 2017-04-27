# -*- coding: utf-8 -*-
import ctypes, sys
from ipaddress import *

def ARP_exists(host):
    """ Envoie une requête ARP who? en direction d'un hôte """

    SendARP = ctypes.windll.Iphlpapi.SendARP
    #inetaddr = ctypes.windll.wsock32.inet_addr(host) #Fonctionne uniquement sous Python 2
    inetaddr = int(IPv4Address('.'.join(host.split(".")[::-1])))

    buffer = ctypes.c_buffer(6)
    addlen = ctypes.c_ulong(ctypes.sizeof(buffer))

    if SendARP(inetaddr, 0, ctypes.byref(buffer), ctypes.byref(addlen)) == 0:
        print(host)
        return 1
    return 0
