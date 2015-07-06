#This is a program to ping across the entire range of IP's for a given
#Flashnet switch, and to list the available IP addresses in both 
#DHCP and static ranges.

#Written by Cory Hinton
#Pinger v1 
#Revision date 7/1/15

import os
import platform
import time
import multiprocessing
import Queue
import threading

#Function to convert an integer to an IP string
def IntToIP (ipRangeInt):
	oct1 = int(ipRangeInt / 16777216) % 256
	oct2 = int(ipRangeInt/ 65536) % 256
	oct3 = int(ipRangeInt / 256) % 256
	oct4 = int(ipRangeInt) % 256
	return '%(oct1)s.%(oct2)s.%(oct3)s.%(oct4)s' % locals()

#Function determines platform, pings address, and returns whether the ping was successful or not
def PingAddr (testAddr):
	
	plat = platform.system()
	ipaddr = IntToIP(testAddr)

	#Look! Cross-platform functionality! All I need is web-based development and cloud, and then I've got myself a tech start-up
	if plat is 'Windows':
		
		response = os.system("ping " + ipaddr)
		
		

	else:
		
		response = os.system("ping -c 4 " + ipaddr)
		
		
		
	#if the ping responds, it returns 0. Since I want ones that don't respond, I want not equal to 0
	
	if response != 0:
		
		return (ipaddr)

	else: 
		
		return
	
	#Thread doesn't seem to be closing. I don't know how to fix this quite yet, but will work on it
	



if __name__ == "__main__":
	#MAIN THREAD
	
	print "Welcome to the CALO Pinger!"
	networkID = raw_input('Please enter the network ID of the BB switch - ')


	#convert Network ID into int number
	netIdArr = map(int,networkID.split("."))
	netIdInt = (16777216 * netIdArr[0]) + (65536 * netIdArr[1]) + (256 * netIdArr[2]) + netIdArr[3] 



	#establish the range for the IP
	ipRangeInt = netIdInt + 31



	#convert IP range back into ip string format

	ipRange = IntToIP(ipRangeInt)


	#define array of ip

	ipArr = []

	#place each IP in array or comparable structure


	for x in range (0, 32):
		newAddr = netIdInt + x
		ipArr.append(newAddr)
		





	#ping across subnet, remove address that are not available
	#This needs to have threading to quickly ping across all addresses
	print "Pinging Addresses...please wait a moment...Go play fooseball or something...."



	#Multiprocessing the function

	#It ALL WORKS. Need to test in lab environ.
	
	pool = multiprocessing.Pool(processes=31)
	
	results = [pool.apply_async(PingAddr, args=(ipArr[x],)) for x in range(1,31)]
	
	
	#windows does not like this part
	output = [p.get() for p in results]
	
	print(output)




	raw_input("Please press Return to close the Window")

