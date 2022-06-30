import ipaddress
ip1=ipaddress.IPv4Address('192.168.1.1')
net1=ipaddress.IPv4Network((ip1,24), strict=False)
print(net1)

for ip in net1:
  #  print(ip)
    print(ip, " ", "multicast", ip.is_multicast)
net1.is_multicast

ip1=ipaddress.IPv4Interface('192.168.1.1/24')
ip2=ipaddress.IPv4Interface('192.168.1.2/24')
traffic={ip1:200, ip2:500}
print(traffic)
print(net1.prefixlen)
print(net1.netmask)
print(net1.network_address)


