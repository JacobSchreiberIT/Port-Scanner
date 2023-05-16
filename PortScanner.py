'''
This file takes in an ip address and prints out which ports are open on the device assosiated to the inputted ip address

Valid arguments would be at the command line, python3 scanner.py [target's ip address]
'''

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) != 2:
	print("Invalid amount of arguements.")
	print("Syntax: python3 scanner.py target")
else: 

	try:
		target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPV4
		
		#Banner
		print("-" * 50)
		print("Scanning target " + target)
		print("Time started: " + str(datetime.now()))
		print("-" * 50)
		
		for port in range(50, 85):
			s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			socket.setdefaulttimeout(1)
			result = s.connect_ex((target,port)) #returns an error indicator; 0 is open 1 is error
			
			if result == 0:
				print("Port {} is open".format(port))
			s.close()
		
		print("-" * 15, "Scanning Complete", "-" * 16)
			
	except KeyboardInterrupt:
		print("\nExiting program")
		sys.exit()
		
	except socket.gaierror:
		print("Hostname could not be resolved.")

	except socket.error:
		print("Couldn't connect to server.")
		sys.exit()
