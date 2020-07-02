import subprocess
import sys
import socket
import time

retry = 1
delay = 0
timeout = 1


def pingLan(subnet, start, end):
    string = "Pinging IP's from " + subnet + "." + str(start) + " to " + subnet + "." + str(end) + "...\n"
    cmd = "echo \"" + string + "\" > results.txt "
    subprocess.call(cmd, shell=True)

    for ping in range(start, (end + 1)):
        address = subnet + "." + str(ping)
        cmd = "ping -c 1 -w 1  " + address + " >> results.txt"
        ps = subprocess.call(cmd, shell=True)
        if ps == 0:
            print("Ping to " + address + "    SUCCESS")
        else:
            print("Ping to " + address + "    FAIL")


def isOpen(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((ip, int(port)))
        s.shutdown(socket.SHUT_RDWR)
        return True
    except:
        return False
    finally:
        s.close()


def checkHost(ip, port):
    ipup = False
    for i in range(retry):
        if isOpen(ip, port):
            ipup = True
            break
        else:
            time.sleep(delay)
    return ipup


def parseArgs(args):
    if len(args) > 1:
        if args[2] == "-ping":
            print("Pinging IP's from " + args[1] + "." + args[3] + " to " + args[1] + "." + args[4] + "...")
            pingLan(args[1], int(args[3]), int(args[4]))
        elif args[2] == "-ports":
            print("Checking " + args[1] + " on ports " + str(args[3]) + " through " + str(args[4]))
            scanPorts(args[1], int(args[3]), int(args[4]))
        else:
            printUsage()
    else:
        printUsage()


def scanPorts(ip, start, end):
    for i in range(start, (end +1)):
        if checkHost(ip, i):
            print("Scan on " + ip + ":" + str(i) + " returned " + "     UP")
        else:
            print("Scan on " + ip + ":" + str(i) + " returned " + "     DOWN")


def printUsage():
    print("USAGE: NewtworkMapper.py <option (ping or port)><subnet> <start> <end>")
    print("Ping Ex: 'NewtworkMapper.py -p 192.168.0 0 255' \n will ping 192.168.0.0 through 192.168.0.255")
    print(
        "Port scan Ex: 'NewtworkMapper.py -p 192.168.0.0 0 443' \n will check ports if ports 0 through 443 are open on 192.168.0.0 ")


parseArgs(sys.argv)
