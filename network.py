import sys
import ipaddress

#print("This is the name of the script: ", sys.argv[0])
#print("Number of arguments: ", len(sys.argv))
#print("The arguments are: " , str(sys.argv))
# s = input("Enter something: ")
# print("You typed ", s)
startIP = ""
if len(sys.argv) > 1:
	startIP = sys.argv[1]
else:
	startIP = input("Enter starting IP (192.1.0.0/32): ")



net = ipaddress.ip_network(startIP)
print(net)
# print(net.prefixlen)

for addr in net.hosts():
    print(addr)

print('---')
    # for i, ip in zip(range(5), net):
    #     print(ip)
print()
    

