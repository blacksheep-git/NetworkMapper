import subprocess
import sys

def pingLan(subnet,start, end):
    ipAddresses = []
    for ping in range(start, (end+1)):
           address = subnet + "." + str(ping)
           cmd = "ping -c 1 " + address + " >> results.txt"
           ps = subprocess.call(cmd, shell=True)
           if ps == 0:
               ipAddresses.append("Ping to " + address + "   SUCCESS")
           else:
               ipAddresses.append("Ping to " + address + "   FAIL")

    return ipAddresses

def mapper(subnet,start, end):
    print("Pinging IP's from " + subnet + "." + str(start) + " to " + subnet + "." + str(end) + " ...")
    list = pingLan(subnet,start, end)
    for i in list:
        print(i)
    print("Done.\n")

def parseArgs(args):
    if len(args) > 1:
        mapper(args[1], int(args[2]), int(args[3]))
    else:
        printUsage()

def printUsage():
    print("USAGE: NewtworkMapper.py <subnet> <start> <end>")
    print("Ex: 'NewtworkMapper.py 192.168.0 0 255' \n will ping 192.168.0.0 through 192.168.0.255")

parseArgs(sys.argv)
