import sys
import ipaddress

print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: " , str(sys.argv))
# s = input("Enter something: ")
# print("You typed ", s)
startIP = ""
if len(sys.argv) > 1:
	startIP = sys.argv[1]
else:
	startIP = input("Enter starting IP (192.1.0.0/32): ")


print(startIP)


NETWORKS = [
    startIP,
    # 'fdfd:87b5:b475:5e3e::/64',
]

for n in NETWORKS:
    net = ipaddress.ip_network(n)
    print('{!r}'.format(net))
    next(net.hosts())
    for x in net.hosts():
    	print(x)

    # for i, ip in zip(range(5), net):
    #     print(ip)
    print()

