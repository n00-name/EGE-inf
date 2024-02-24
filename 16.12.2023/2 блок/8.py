import ipaddress as ip

count = 0
ips = ip.ip_network(f'158.132.161.128/255.255.255.128', False)

for ip_ in ips:
    bite = int(str(ip_).split('.')[-1])
    bin_bite = bin(bite)[2:]
    bit = bin_bite[-1]

    if bit == '1':
        count += 1

    print(ip_, bite, bin_bite, bit)

print(count)
