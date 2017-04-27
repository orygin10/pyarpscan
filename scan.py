# -*- coding: utf-8 -*-
from ip_tools import *
from arp import *
from multiprocessing.dummy import Pool as ThreadPool

if __name__ == '__main__':
    ip = getIPv4Address()
    netmask = getNetmask()
    network = getNetwork(ip, netmask)

    hosts = list(map(str,network.hosts()))

    # Fait un pool de workers
    pool = ThreadPool(256)

    # Ouvre une requête ARP dans chaque thread
    results = pool.map(ARP_exists, hosts)

    pool.close()
    pool.join()
