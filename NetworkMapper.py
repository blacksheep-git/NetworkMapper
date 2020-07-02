import subprocess
import sys

def pingLan(subnet,start, end):
    string = "Pinging IP's from " + subnet + "." + str(start) + " to " + subnet + "." + str(end) + "...\n"
    cmd = "echo \"" + string + "\" > results.txt "
    subprocess.call(cmd, shell=True)

    for ping in range(start, (end+1)):
           address = subnet + "." + str(ping)
           cmd = "ping -c 1 -w 1  " + address + " >> results.txt"
           ps = subprocess.call(cmd, shell=True)
           if ps == 0:
               print("Ping to " + address + "    SUCCESS")
           else:
               print("Ping to " + address + "    FAIL")

def parseArgs(args):
    if len(args) > 1:
        print("Pinging IP's from " + args[1] + "." + args[2] + " to " + args[1] + "." + args[3] + "...")
        pingLan(args[1], int(args[2]), int(args[3]))
    else:
        printUsage()

def printUsage():
    print("USAGE: NewtworkMapper.py <subnet> <start> <end>")
    print("Ex: 'NewtworkMapper.py 192.168.0 0 255' \n will ping 192.168.0.0 through 192.168.0.255")

parseArgs(sys.argv)
