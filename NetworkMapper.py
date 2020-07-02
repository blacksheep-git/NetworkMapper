import subprocess

ipAddresses = []


def pingLan(subnet,start, end):
    for ping in range(start, (end+1)):
        address = subnet + "." + str(ping)
        cmd = "ping -c 1 " + address + " > results.txt"
        ps = subprocess.call(cmd, shell=True)
        if ps <= 0:
            ipAddresses.append(address)

def mapper(subnet,start, end):
    retVal = ""
    pingLan(subnet,start, end)
    for i in ipAddresses:
        retVal += "ping to " + i + "   OK\n"
    return retVal

print(mapper("216.128.235", 1, 2))

print(mapper("127.0.0", 1, 10))
