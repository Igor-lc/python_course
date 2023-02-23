import ipaddress


def has_access(ip, network):
    return ipaddress.ip_address(ip) in list(ipaddress.ip_network(network).hosts())


access = has_access("91.142.84.30", "91.142.84.0/27")
print(access)

# in в списках та ітераторах
