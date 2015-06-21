#This is a program to ping across the entire range of IP's for a given
#Flashnet switch, and to list the available IP addresses in both 
#DHCP and static ranges.

#Written by Cory Hinton
#Pinger v1 
#Revision date 6/10/15

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
def PingAddr (ipaddr, openAddrs):
	plat = platform.system()

	#Look! Cross-platform functionality! All I need is web-based development and cloud, and then I've got myself a tech start-up
	if plat is 'Windows':
		response = os.system("ping " + ipaddr)
		
		

	else:
		response = os.system("ping -c 4 " + ipaddr)
		
	#if the ping responds, it returns 0. Since I want ones that don't respond, I want not equal to 0
	
	if response != 0: 
		openAddrs.put(ipaddr)
	print "thread end"
	#Thread doesn't seem to be closing. I don't know how to fix this quite yet, but will work on it
	return




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

#testing that list worked
#for x in range (0, 32):
#	addr = ipArr[x]
#	print (IntToIP(addr))



#ping across subnet, remove address that are not available
#This needs to have threading to quickly ping across all addresses
print "Pinging Addresses...please wait a moment...Go play fooseball or something...."

#openAddrs = []

#testing pring command
#os.system("ping -c 4 8.8.8.8")
#for x in range (1, 32):
#	testAddr = IntToIP(ipArr[x])
#
#	if PingAddr(testAddr) == 0:
#		openAddrs.append(testAddr)


#Multiprocessing the function
#This only returns the last available address. Not ideal, but working.
#need to figure out how to store available address into a list
#I switched to multiprocessing, and now working on both OS. It still doesn't seem to exit the loop, but progress is progress.
openAddrs = multiprocessing.Queue()
for x in range (1, 30):

	testAddr = IntToIP(ipArr[x])
	
	#spawns the thread
	#t = threading.Thread(target=PingAddr, args = (testAddr, openAddrs))
	#t.setDaemon(True)
	#t.start()

	#Trying with multiprocessing instead of threads
	m = multiprocessing.Process(target=PingAddr, args=(testAddr, openAddrs))
	m.start()

	
	
	

	
print "Exiting threading loop"	
	
#s = openAddrs.get()
#print s





#print all available addresses
#for addr in openAddrs:
#	print addr

raw_input("Please press Return to close the Window")

