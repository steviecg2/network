import textfsm

show_access_list = """
Extended IP access list outside_acl
    10 permit icmp any any (2680779 matches)
    20 permit udp any eq domain any (88 matches)
    30 permit tcp any eq domain any (1445 matches)
    40 permit udp any eq bootps any (1268 matches)
    50 permit udp any any eq isakmp (5165 matches)
    60 permit udp any any eq non500-isakmp (6360519 matches)
    70 permit udp any eq non500-isakmp any
    80 permit tcp any any eq 8443 (903 matches)
    90 permit tcp any any eq 443 (267211 matches)
    100 permit udp any any eq 443 (144 matches)
    110 permit udp any any eq 8443
    120 permit tcp any any range 8000 8020 (1024900 matches)
    130 permit tcp any any established (23275 matches)
"""


