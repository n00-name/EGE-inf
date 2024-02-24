import ipaddress as ip

count = 0
ips = ip.ip_network(f'192.168.248.176/255.255.255.240', False)

for ip_ in ips:
    bin_ = bin(int(ip_))[2:]

    if bin_.count('1') > bin_.count('0'):
        count += 1

    print(ip_, bin_)
print(count)
