# -*- coding: utf-8 -*-
import ipaddress, socket

def getNetwork(ip, netmask):
    return ipaddress.IPv4Network("%s/%s" % (ip, netmask), strict=False)

def getIPv4Address():
    ip_found = socket.gethostbyname(socket.gethostname())
    print ("Ouvrez une invite de commandes Windows et entrez ipconfig")
    ip_input = input("Appuyez sur ENTRER si votre adresse IPv4 est %s, sinon ecrivez-la : " % ip_found)
    if ip_input == '':
        return ip_found
    else:
        try:
            return ipaddress.IPv4Address(ip_input)
        except ValueError:
            print ("%s n'est pas une adresse IPv4 valide ..." % ip_input)

def getNetmask():
    netmask_default = "255.255.255.0"
    netmask_input = input("Appuyez sur ENTRER si votre masque de sous-réseau est %s, sinon ecrivez-le : " % netmask_default)
    if netmask_input == '':
        return netmask_default
    else:
        try:
            return ipaddress.IPv4Address(netmask_input)
        except ValueError:
            print ("%s n'est pas un masque de sous-réseau valide ..." % netmask_input)
