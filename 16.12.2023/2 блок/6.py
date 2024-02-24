import ipaddress as ip

count = 0
arr = [1, 3, 7, 15, 31, 63, 127, 255]
ips = ip.ip_network(f'139.75.100.0/255.255.252.0', False)

for ip_ in ips:
    bite = int(str(ip_).split('.')[-1])
    print(ip_, bite)

    if bite in arr:
        count += 1

print(count)
