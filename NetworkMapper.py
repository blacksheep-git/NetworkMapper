import subprocess



def pingLan(live, subnet,start, end):
    ipAddresses = []
    if live:
        for ping in range(start, (end+1)):
            address = subnet + "." + str(ping)
            cmd = "ping -c 1 " + address + " >> results.txt"
            ps = subprocess.call(cmd, shell=True)
            if ps == 0:
                ipAddresses.append("ping to " + address + "   SUCCESS")
    else:
        for ping in range(start, (end+1)):
            address = subnet + "." + str(ping)
            cmd = "ping -c 1 " + address + " >> results.txt"
            ps = subprocess.call(cmd, shell=True)
            if ps > 0:
                ipAddresses.append("ping to " + address + "   FAIL")

    return ipAddresses

def mapper(live,subnet,start, end):
    print("These IP's from " + subnet + "." + str(start) + " -> " + subnet + "." + str(end) + " are live:")
    list = pingLan(live, subnet,start, end)
    for i in list:
        print(i)
    print("\n")

mapper(False, "216.128.235", 1, 33)
mapper(True, "216.128.235", 1, 33)

#print(mapper(True, "127.0.0", 1, 10))
