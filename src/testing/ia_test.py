import ipaddress

# Create an IPv4 network object with a netmask of 0.0.0.0
network = ipaddress.IPv4Network('192.168.0.0')

# Calculate the default CIDR notation by counting the number of leading zeros in the binary representation of the netmask
cidr = str(bin(int(network.netmask)))[2:].count('0')

# Print the CIDR notation
print(cidr)
