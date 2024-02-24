import ipaddress as ip

count = 0
ips = ip.ip_network(f'142.108.56.118/255.255.255.240', False)

for ip_ in ips:
    bin_ = bin(int(ip_))[2:]
    bin12 = bin_[:16]
    bin34 = bin_[16:]

    if bin12.count('1') < bin34.count('1'):
        count += 1

    print(ip_, bin_)
print(count)
