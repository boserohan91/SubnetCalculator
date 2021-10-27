import sys
import random

def subnet_calc():

    try:
        #check IP address validity
        ip = input("Enter IP address: ")
        octet_list = ip.split(".")

        if not (len(octet_list) == 4) and (1 <= int(octet_list[0]) <= 223) and (int(octet_list[0]) != 127) and (int(octet_list[0]) != 169 
            or int(octet_list[1]) != 254) and (0 <= int(octet_list[1]) <= 255 and 0 <= int(octet_list[2]) <= 255 
            and 0 <= int(octet_list[3]) <= 255):
            print(f"Invalid IP address: {ip}")
            sys.exit()

        #check subnet mask validity
        masks = [255, 254, 252, 248, 240, 224, 192, 128, 0]
        
        subnet_mask = input("Enter subnet mask: ")

        subnet_octet = subnet_mask.split(".")

        if not (len(subnet_octet) == 4) and (int(subnet_octet[0]) == 255) and (int(subnet_octet[1]) in masks) and (int(subnet_octet[2]) in masks) \
            and (int(subnet_octet[3] in masks)) and (int(subnet_octet[1]) >= int(subnet_octet[2]) >= int(subnet_octet[3]) ) :
            print(f"* Invalid subnet mask address: {subnet_mask}")
            sys.exit()

        subnet_mask_binary_list = []
        wildcard_mask_list = []

        for octet in subnet_octet:
            binary_octet = bin(int(octet)).lstrip('0b')
            subnet_mask_binary_list.append(binary_octet.zfill(8))

            wildcard_octet = 255 - int(octet)
            wildcard_mask_list.append(str(wildcard_octet))


        subnet_mask_binary = "".join(subnet_mask_binary_list)
        wildcard_mask_binary = ".".join(wildcard_mask_list)

        print(f'subnet_mask_binary = {subnet_mask_binary}')
        print(f'wildcard_mask_binary = {wildcard_mask_binary}')

        no_of_zeros = subnet_mask_binary.count("0")
        no_of_ones = 32 - no_of_zeros
        no_of_hosts = abs(2 ** no_of_zeros - 2)

        print(f"no_of_zeros= {no_of_zeros}")
        print(f"no_of_ones= {no_of_ones}")
        print(f"no_of_hosts= {no_of_hosts}")

        binary_ip_octet_list = []

        for octet in octet_list:
            binary_octet = bin(int(octet)).lstrip("0b")

            binary_ip_octet_list.append(binary_octet.zfill(8))

        binary_ip = "".join(binary_ip_octet_list)

        network_address_binary = binary_ip[:no_of_ones] + "0" * no_of_zeros
        bcast_address_binary = binary_ip[:no_of_ones] + "1" * no_of_zeros

        

        net_addr_list = []
        bcast_addr_list = []

        for bit in range(0,32,8):
            net_addr_list.append(str(int(network_address_binary[bit:bit+8],2)))
            bcast_addr_list.append(str(int(bcast_address_binary[bit:bit+8],2)))

        network_address = ".".join(net_addr_list)
        broadcast_address = ".".join(bcast_addr_list)

        print(f"Network Address= {network_address}")
        print(f"Broadcast Address= {broadcast_address}")

        while True:

            response = input("Do you want a random generated address for this network? (y/n)")

            if response == "y":
                generated_ip_addr_list = []

                for index in range(0,4):
                    if net_addr_list[index] == bcast_addr_list[index]:
                        generated_ip_addr_list.append(net_addr_list[index])
                    else:
                        generated_ip_addr_list.append(str(random.randint(int(net_addr_list[index]),int(bcast_addr_list[index]))))

                generated_ip_addr = ".".join(generated_ip_addr_list)

                print(generated_ip_addr)

                continue
            else:
                print("\nProgram Terminated..")
                break


    except KeyboardInterrupt:
        print("\nExiting program...")
        sys.exit()


def main():
    subnet_calc()


if __name__ == "__main__":
    main()