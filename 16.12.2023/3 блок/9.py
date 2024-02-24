import ipaddress as ip

count = 0
ips = ip.ip_network(f'202.75.38.152/255.255.255.248', False)

for ip_ in ips:
    bin_ = bin(int(ip_))[2:]

    if '111' in bin_:
        count += 1

    print(ip_, bin_)
print(count)
