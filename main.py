import sys
import socket
from datetime import datetime

target = input("Please specify your target ipV4 Address: ") #Designate Target IPv4 Address
print('\n')
print("Mode 0: Standard Sniffing")
print("Mode 1: Debug Connection Mode")
mode = input("please select mode 0 or 1: ")

print("-=" * 50) #Informtaion for user
print("Scanning Target: " + target)
print("Selecting {} mode".format(mode))
print("Scanning started at:" + str(datetime.now()))
print("-=" * 50)
  
try: #Try to run and catch error
     
    # will scan ports between 1 to 15,000
    for port in range(1,15000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.25)
        # returns an error indicator
        result = s.connect_ex((target,port))
        if result ==0: #Returns information if connection was established
            print("Port {} is open".format(port))
        elif mode == "1":
            print("Port {} is closed".format(port))
        s.close()
         
except KeyboardInterrupt: #Error Captures
        print("\n Exiting Program")
        sys.exit()
except socket.gaierror:
        print("\n Address Could Not Be Found")
        sys.exit()
except socket.error:
        print("\n Device Unresponsive")
        sys.exit()
