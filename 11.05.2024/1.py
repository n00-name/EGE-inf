import ipaddress as ip

count = 0
ips = ip.ip_network('216.130.64.0/255.255.192.0', False)

for ip_ in ips.hosts():
    bits = list(map(int, str(ip_).split('.')))

    if all(bit % 2 == 0 for bit in bits):
        count += 1

print(count)

import ipaddress as ip

count = 0
ips = ip.ip_network('216.130.64.0/255.255.192.0', False)

for ip_ in ips:
    print(ip_)
    bits = list(map(int, str(ip_).split('.')))

    if all(bit % 2 == 0 for bit in bits):
        count += 1

print(count)
