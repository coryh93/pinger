#This is a program to ping across the entire range of IP's for a given
#Flashnet switch, and to list the available IP addresses in both 
#DHCP and static ranges.

#Written by Cory Hinton
#Pinger v1 
#Revision date 5/31/15


#Function to convert an integer to an IP string
def IntToIP (ipRangeInt):
	oct1 = int(ipRangeInt / 16777216) % 256
	oct2 = int(ipRangeInt/ 65536) % 256
	oct3 = int(ipRangeInt / 256) % 256
	oct4 = int(ipRangeInt) % 256
	return '%(oct1)s.%(oct2)s.%(oct3)s.%(oct4)s' % locals()


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



#print all available addresses



