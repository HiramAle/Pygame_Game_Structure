import ipaddress
import math
import random
from tabulate import tabulate


def generate_random_ip() -> tuple[str, str, int]:
    ip_classes = {"A": 8, "B": 16, "C": 24}
    selected_class = random.choice(list(ip_classes.keys()))
    if selected_class == "A":
        random_ip = str(random.randint(1, 126)) + ".0.0.0"
    elif selected_class == "B":
        random_ip = str(random.randint(128, 191)) + "." + str(random.randint(0, 255)) + ".0.0"
    elif selected_class == "C":
        random_ip = str(random.randint(192, 223)) + "." + str(random.randint(0, 255)) + "." + str(
            random.randint(0, 255)) + ".0"
    else:
        random_ip = ""

    return random_ip, selected_class, ip_classes[selected_class]


def subnetor():
    random_ip, ip_class, default_cidr = generate_random_ip()
    network = ipaddress.IPv4Network(f"{random_ip}/{default_cidr}")
    subnets_needed = random.randint(2, 8)
    bits_borrowed = math.ceil(math.log(subnets_needed, 2))
    new_cidr = default_cidr + bits_borrowed
    headers = ["No. Subnet", "Subnet Id", "First Usable", "Broadcast"]
    data = []

    for index, subnet in enumerate(network.subnets(new_prefix=new_cidr)):
        first_usable = subnet[1]
        line = [index + 1, subnet.network_address, first_usable, subnet.broadcast_address]
        data.append(line)

    print("Network:", network.network_address)
    print("Default mask:", network.netmask)
    print("Subnets needed:", subnets_needed)
    print("Total subnets:", 2 ** bits_borrowed)
    print(tabulate(data, headers=headers, tablefmt="grid"))


if __name__ == '__main__':
    subnetor()
