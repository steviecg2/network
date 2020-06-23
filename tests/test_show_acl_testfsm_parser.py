from prettytable import PrettyTable
import json
import os
import textfsm

directory = os.path.dirname(os.path.realpath(__file__))
template = open(f"{directory}/../parsers/cisco_ios_show_access-list.test")
output = """
Extended IP access list labvpn_acl
    10 permit ip 10.0.0.0 0.0.255.255 10.0.0.0 0.0.255.255
    20 permit ip 142.100.64.0 0.0.1.255 10.0.0.0 0.0.255.255
    30 permit ip 142.200.64.0 0.0.1.255 10.0.0.0 0.0.255.255
    40 permit ip 142.101.64.0 0.0.1.255 10.0.0.0 0.0.255.255
    50 permit ip 142.102.64.0 0.0.1.255 10.0.0.0 0.0.255.255
Extended IP access list nat_acl
    10 deny ip any 10.0.0.0 0.255.255.255
    20 deny ip any 172.16.0.0 0.15.255.255
    30 deny ip any 192.168.0.0 0.0.255.255
    40 permit ip 10.0.0.0 0.255.255.255 any
    50 permit ip 172.16.0.0 0.15.255.255 any
    60 permit ip 198.168.0.0 0.0.255.255 any
    70 permit ip 142.100.64.0 0.0.1.255 any
    80 permit ip 142.101.64.0 0.0.1.255 any
    90 permit ip 142.102.64.0 0.0.1.255 any
    100 permit ip 142.200.64.0 0.0.1.255 any
Extended IP access list outside_acl
    10 permit icmp any any
    20 permit udp any eq domain any
    30 permit tcp any eq domain any
    40 permit udp any eq bootps any
    50 permit udp any any eq isakmp
    60 permit udp any any eq non500-isakmp
    70 permit udp any eq non500-isakmp any
    80 permit tcp any any eq 8443
    90 permit tcp any any eq 443
    100 permit udp any any eq 443
    110 permit udp any any eq 8443
    120 permit tcp any any range 8000 8020
    130 permit tcp any any established
"""
# port should be source_operator
# sn should be sequence_number
# range should be source_port
# modified needs additional logic
#   elimiinate matches
#   derive a destination operator
#   derive a destination port
#   derive l4_established
#   derive logging

template = textfsm.TextFSM(template)
output = template.ParseText(output)
table = PrettyTable(template.header)
for row in output:
    table.add_row(row)
print(table)
