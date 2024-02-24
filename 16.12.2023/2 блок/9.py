import ipaddress as ip

count = 0
ips = ip.ip_network(f'140.19.96.0/255.255.248.0', False)

for ip_ in ips:
    bite = str(ip_).split('.')
    bin_bite = [bin(int(x))[2:] for x in bite]

    count_ones = bin_bite[0].count('1')

    all_equal = all(elem.count('1') == count_ones for elem in bin_bite)

    if all_equal == True:
        count += 1

    print(ip_, bite, bin_bite, all_equal)

print(count)
