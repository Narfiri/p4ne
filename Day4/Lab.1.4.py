import ipaddress
import random
print(random.randint(8,24))
print(ipaddress.IPv4Network(random.randint(0x0B000000,0xDF000000)))


class IPv4RandomNetwork(ipaddress.IPv4Network):
    def __init__(self, n="0.0.0.0", p="/0", gw="0.0.0.0"):
        ipaddress.IPv4Network.__init__(self, (random.randint(0x0B000000, 0xDF000000), random.randint(8, 24)), strict=False)

for i in range (0,50):
    rn = IPv4RandomNetwork()
    print(rn)
 #   k = int(rn.netmask)*2**32+int(rn.network_address)
  #  print(k)
  #  print(rn.network_address)
 # print(rn.netmask)

#ef sortfunk(x)
# return x.key:value







