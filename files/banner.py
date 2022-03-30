import os
from files.colors import r , g , w , c , y

logo = f"""
 ▄█     █▄   ▄█  ███▄▄▄▄   ████████▄   ▄██████▄   ▄█     █▄     ▄████████ 
███     ███ ███  ███▀▀▀██▄ ███   ▀███ ███    ███ ███     ███   ███    ███ 
███     ███ ███▌ ███   ███ ███    ███ ███    ███ ███     ███   ███    █▀  
███     ███ ███▌ ███   ███ ███    ███ ███    ███ ███     ███   ███        
███     ███ ███▌ ███   ███ ███    ███ ███    ███ ███     ███ ▀███████████ 
███     ███ ███  ███   ███ ███    ███ ███    ███ ███     ███          ███ 
███ ▄█▄ ███ ███  ███   ███ ███   ▄███ ███    ███ ███ ▄█▄ ███    ▄█    ███ 
 ▀███▀███▀  █▀    ▀█   █▀  ████████▀   ▀██████▀   ▀███▀███▀   ▄████████▀  
                                                                          
    ███        ▄████████  ▄██████▄       ▄█    ▄████████ ███▄▄▄▄          
▀█████████▄   ███    ███ ███    ███     ███   ███    ███ ███▀▀▀██▄        
   ▀███▀▀██   ███    ███ ███    ███     ███   ███    ███ ███   ███        
    ███   ▀  ▄███▄▄▄▄██▀ ███    ███     ███   ███    ███ ███   ███        
    ███     ▀▀███▀▀▀▀▀   ███    ███     ███ ▀███████████ ███   ███        
    ███     ▀███████████ ███    ███     ███   ███    ███ ███   ███        
    ███       ███    ███ ███    ███     ███   ███    ███ ███   ███        
   ▄████▀     ███    ███  ▀██████▀  █▄ ▄███   ███    █▀   ▀█   █▀         
              ███    ███            ▀▀▀▀▀▀                                                                 
"""

lololo = f"""
    ███        ▄████████  ▄██████▄       ▄█    ▄████████ ███▄▄▄▄                      
▀█████████▄   ███    ███ ███    ███     ███   ███    ███ ███▀▀▀██▄                    
   ▀███▀▀██   ███    ███ ███    ███     ███   ███    ███ ███   ███                    
    ███   ▀  ▄███▄▄▄▄██▀ ███    ███     ███   ███    ███ ███   ███                    
    ███     ▀▀███▀▀▀▀▀   ███    ███     ███ ▀███████████ ███   ███                    
    ███     ▀███████████ ███    ███     ███   ███    ███ ███   ███                    
    ███       ███    ███ ███    ███     ███   ███    ███ ███   ███                    
   ▄████▀     ███    ███  ▀██████▀  █▄ ▄███   ███    █▀   ▀█   █▀                     
              ███    ███            ▀▀▀▀▀▀                                            
 ▄████████    ▄████████    ▄████████    ▄████████     ███      ▄██████▄     ▄████████ 
███    ███   ███    ███   ███    ███   ███    ███ ▀█████████▄ ███    ███   ███    ███ 
███    █▀    ███    ███   ███    █▀    ███    ███    ▀███▀▀██ ███    ███   ███    ███ 
███         ▄███▄▄▄▄██▀  ▄███▄▄▄       ███    ███     ███   ▀ ███    ███  ▄███▄▄▄▄██▀ 
███        ▀▀███▀▀▀▀▀   ▀▀███▀▀▀     ▀███████████     ███     ███    ███ ▀▀███▀▀▀▀▀   
███    █▄  ▀███████████   ███    █▄    ███    ███     ███     ███    ███ ▀███████████ 
███    ███   ███    ███   ███    ███   ███    ███     ███     ███    ███   ███    ███ 
████████▀    ███    ███   ██████████   ███    █▀     ▄████▀    ▀██████▀    ███    ███ 
             ███    ███                                                    ███    ███ 
                                            
                                            {y}<{w}/{y}> {c}Author: {w}Saad Khan     
"""
from files.colors import *


def banner():
    print(ran + lololo)
    print(c.ran,"\n" + "|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX, "- " * 4, " [+] Follow me on Instagram @cyber_dioxide ", "- " * 4 + c.ran + "|")
    print(c.ran, "\n" + "|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX, "- " * 4, " [+] Follow me on Instagram @cyber_dioxide ", "- " * 4+c.ran + "|")
    print(c.ran , "\n"+ "|"+ Style.BRIGHT + Fore.LIGHTRED_EX, "- " * 4, "[+] Github: https://github.com/Cyber-Dioxide/Stock-Termux ", "- " * 3+c.ran + "|")


def banner2():
    print(c.ran,"\n" + "|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX, "- " * 4, " [+] Follow me on Instagram @cyber_dioxide ", "- " * 4 + c.ran + "|")
    print(c.ran, "\n" + "|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX, "- " * 4, " [+] Follow me on Instagram @cyber_dioxide ", "- " * 4+c.ran + "|")
    print(c.ran , "\n"+ "|"+ Style.BRIGHT + Fore.LIGHTRED_EX, "- " * 4, "[+] Github: https://github.com/Cyber-Dioxide/Stock-Termux ", "- " * 3+c.ran + "|")

def clear():
    os.system("clear")
