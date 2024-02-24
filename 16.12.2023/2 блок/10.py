import ipaddress as ip

found = False
min_b = None

for i in range(256):
    ips = ip.ip_network(f'64.129.{str(i)}.10/255.255.252.0', False)
    condition_met = True

    for ip_ in ips:
        bins_ = bin(int(ip_))[2:]
        a = bins_[:16]
        aa = bins_[16:]

        if not (a.count('1') <= aa.count('1')):
            condition_met = False
            break

    if condition_met:
        found = True
        min_b = i
        break

if found:
    print(f"Found the minimum b: {min_b}")
else:
    print("No such b found.")