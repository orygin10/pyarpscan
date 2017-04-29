# -*- coding: utf-8 -*-
"""Main script for pyarpscan package"""
from multiprocessing.dummy import Pool as ThreadPool
from ip_tools import calc_network, ask_for_ip, ask_for_netmask
from arp import arp_host

def main():
    """pyarpscan top-level code
    Fetch IP address and network mask and compute network address
    Make hosts list from IPv4Network() object
    Open an ARP request in 256 threads towards 256 hosts at a time.
    """

    ip_address = ask_for_ip()
    netmask = ask_for_netmask()
    network = calc_network(ip_address, netmask)

    hosts = list(map(str, network.hosts()))

    # Fait un pool de workers
    pool = ThreadPool(256)

    # Ouvre une requête ARP dans chaque thread
    pool.map(arp_host, hosts)
    input("Fin.")

    pool.close()
    pool.join()

if __name__ == '__main__':
    main()
