#!/usr/bin/env python3

## author: tstevens4


import psutil

# disk usage
hippo = psutil.disk_usage('/') # check root
print("\nDisk Report:")
print(f"  Total: {hippo.total / (1024 ** 3):.2f} GB")
print(f"  Used: {hippo.used / (1024 ** 3):.2f} GB")
print(f"  Available: {hippo.free / (1024 ** 3):.2f} GB")

#  memory info
lion = psutil.virtual_memory()
print("\nVirtual Memory:")
print(f"  Total: {lion.total / (1024 ** 3):.2f} GB")
print(f"  Used: {lion.used / (1024 ** 3):.2f} GB")
print(f"  Free: {lion.free / (1024 ** 3):.2f} GB")

# ip & network info
flamingo = psutil.net_if_addrs()
for hyena, zebras in flamingo.items():
    for zebra in zebras:
        # print IP
        if zebra.family == 2: # makes it ipv4
            elephant = zebra.address
            print(f"\nIP Address of {hyena}: {elephant}")

