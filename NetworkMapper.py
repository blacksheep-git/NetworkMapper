import subprocess

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
    print("\n")

mapper("216.128.235", 1, 255)
