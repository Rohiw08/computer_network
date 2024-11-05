import ipaddress
import math

def calculate_subnet_mask(ip_address, num_subnets=None, num_hosts=None):
    # Convert IP address to IPv4 object
    network = ipaddress.IPv4Network(ip_address, strict=False)
    print(f"Original Network: {network}")

    # Calculate the number of bits to borrow for subnets or to satisfy hosts requirement
    if num_subnets:
        bits_for_subnets = math.ceil(math.log2(num_subnets))
        new_prefix_len = network.prefixlen + bits_for_subnets
    elif num_hosts:
        bits_for_hosts = math.ceil(math.log2(num_hosts + 2))  # Adding 2 for network and broadcast addresses
        new_prefix_len = 32 - bits_for_hosts
    else:
        print("Either number of subnets or number of hosts must be provided.")
        return

    # Calculate the new subnet mask
    if new_prefix_len > 32:
        print("Error: Too many subnets or too few hosts for this network.")
        return

    subnet_mask = ipaddress.IPv4Network(f"0.0.0.0/{new_prefix_len}").netmask
    print(f"New Subnet Mask: {subnet_mask}")
    
    # Calculate number of subnets and hosts per subnet
    total_subnets = 2 ** (new_prefix_len - network.prefixlen)
    total_hosts_per_subnet = 2 ** (32 - new_prefix_len) - 2

    print(f"Total Subnets: {total_subnets}")
    print(f"Hosts per Subnet: {total_hosts_per_subnet}")
    
    # List all subnets
    subnets = list(network.subnets(new_prefix=new_prefix_len))
    print("\nSubnets:")
    for subnet in subnets:
        print(subnet)

# Input: IP Address in CIDR notation, number of subnets or hosts
ip_address = "192.168.1.0/24"  # Example IP
num_subnets = 8  # Number of subnets (for demonstration, you can change this value)
calculate_subnet_mask(ip_address, num_subnets=num_subnets)
