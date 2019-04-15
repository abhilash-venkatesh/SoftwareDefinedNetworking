import requests
import json
from tabulate import *
from get_ticket import *
from print_devices import *
from print_hosts import *
from path_trace import *

print("This Python Script  <--REST APIs-->  Cisco APIC-EM  <--SNMP/SSH/TELNET-->  test_network")
print("The hosts in the test network are : ")
print_hosts()
print("The devices in the test network are : ")
print_devices()
while(True):
    print("Enter src_ip and dst_ip to trace path (enter q to quit)")
    srcip = input("src_ip : ")
    if srcip=='q' or srcip=='quit' :
        break
    dstip = input("dst_ip : ")
    if dstip=='q' or dstip=='quit' :
        break
    path_trace(srcip,dstip)
    
