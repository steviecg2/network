import json
import os
import textfsm

directory = os.path.dirname(os.path.realpath(__file__))
template = open(f"{directory}/../parsers/cisco_ios_show_access-list.template")
output = 
"""
Extended IP access list auto_test
    10 deny ip host 1.1.1.1 host 1.1.1.2 log
    20 deny tcp any eq telnet 1.2.3.0 0.0.0.255 range 555 560
    30 permit tcp 5.5.5.0 0.0.0.255 gt 12345 10.0.0.0 0.255.255.255 eq smtp established
    40 deny udp host 4.4.4.4 any lt 5000 log-input
    50 deny icmp any any mask-reply
    60 permit tcp object-group test_obj range 40 www 10.0.0.0 0.255.255.255 eq www pop2 pop3
"""
current = 
"""
['NAME', 'SN', 'ACTION', 'PROTOCOL', 'SOURCE', 'PORT', 'RANGE', 'DESTINATION', 'MODIFIER']
['auto_test', '10', 'deny', 'ip', 'host 1.1.1.1', '', '', 'host 1.1.1.2', 'log']
['auto_test', '20', 'deny', 'tcp', 'any', 'eq', 'telnet', '1.2.3.0 0.0.0.255', 'range 555 560']
['auto_test', '30', 'permit', 'tcp', '5.5.5.0 0.0.0.255', 'gt', '12345', '10.0.0.0 0.255.255.255', 'eq smtp established']
['auto_test', '40', 'deny', 'udp', 'host 4.4.4.4', '', '', 'any', 'lt 5000 log-input']
['auto_test', '50', 'deny', 'icmp', 'any', '', '', 'any', 'mask-reply']
"""
expected = 
"""
['NAME',        'SN', 'ACTION', 'PROTOCOL', 'SOURCE',               'PORT', 'RANGE',    'DESTINATION',              'MODIFIER']
['auto_test',   '10', 'deny',   'ip',       'host 1.1.1.1',         '',     '',         'host 1.1.1.2',             'log']
['auto_test',   '20', 'deny',   'tcp',      'any',                  'eq',   'telnet',   '1.2.3.0 0.0.0.255',        'range 555 560']
['auto_test',   '30', 'permit', 'tcp',      '5.5.5.0 0.0.0.255',    'gt',   '12345',    '10.0.0.0 0.255.255.255',   'eq smtp established']
['auto_test',   '40', 'deny',   'udp',      'host 4.4.4.4',         '',     '',         'any',                      'lt 5000 log-input']
['auto_test',   '50', 'deny',   'icmp',     'any',                  '',     '',         'any',                      'mask-reply']
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
print(json.dumps(output, indent=4))
