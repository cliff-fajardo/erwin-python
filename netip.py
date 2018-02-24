import sys
import ipaddress

#################################################
# Function for creating the available subnet range
#################################################
def subnet_range(start_subnet, end_subnet):
    start = ipaddress.ip_network(start_subnet)
    end = ipaddress.ip_network(end_subnet)
    # print(start.prefixlen)
    # print(list(end))

    assert start.prefixlen == end.prefixlen
    ranges = [
        n
        for ipaddr in ipaddress.summarize_address_range(
            list(start)[0],
            list(end)[0])
        for n in ipaddr.subnets(new_prefix=start.prefixlen)][:-1]
    ranges.append(end)
    return ranges


#################################################
# Output message displayed. {} are placeholders IPs & ticket number
#################################################
output_message = 'santaclara10-1001-i10-swi-1-lo0 {} NANR-us-santaclara10-1001-i10-swi-1-loopback-({})'

# start_subnet = "10.12.0.0/19"
# end_subnet = "10.100.0.0/19"
# num_devices = 5

#################################################
# 1. Get starting subnet
# Check if its passed as a command line argument
#################################################
if len(sys.argv) > 1:
	start_subnet = sys.argv[1]
else:
	start_subnet = input("Enter starting subnet (192.1.0.0/32): ")


#################################################
# 2. Get number of devices 
# Check if its passed as a command line argument
#################################################
if len(sys.argv) > 2:
	num_devices = sys.argv[2]
else:
	num_devices = input("Enter number of devices: ")

ndevices = int(num_devices)

#################################################
# 3. Get ticket number
# Check if its passed as a command line argument
#################################################
if len(sys.argv) > 3:
	ticket_number = sys.argv[3]
else:
	ticket_number = input("Enter ticket number: ")



#################################################
# 4. Create an IP Network object
#################################################
net = ipaddress.ip_network(start_subnet)


#################################################
# 5. If IPv4 - split the octets, increment 3rd octet for use as end subnet
#################################################
if(net.version == 4):
	a,b,c,d = start_subnet.split(".")
	if(net.prefixlen > 24):
		c_next = int(c) + 2

	if(net.prefixlen <= 24):
		c_next = int(c) + 255

	end_subnet_chr = '{}.{}.{}.{}'
	end_subnet = end_subnet_chr.format(a,b,c_next,d)





i = 0
print()
while(i<ndevices):
	ip_out = subnet_range(start_subnet, end_subnet)[i]
	print(output_message.format(ip_out, ticket_number))
	i = i+1

print()

# for r in subnet_range(start_subnet, end_subnet):
# 	print(r)
		# print(n)