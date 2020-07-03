import subprocess
import sys
import socket
import time
from Tkinter import *
import tkMessageBox
import threading

retry = 1
delay = 0
timeout = 1
appName = "NetworkMapper"


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


def parseArgs(args, name):
    if len(args) > 1:
        if args[2] == "-ping":
            print("Pinging IP's from " + args[1] + "." + args[3] + " to " + args[1] + "." + args[4] + "...\n")
            pingLan(args[1], int(args[3]), int(args[4]))
        elif args[2] == "-ports":
            print("Checking " + args[1] + " on ports " + str(args[3]) + " through " + str(args[4]) + "...\n")
            scanPorts(args[1], int(args[3]), int(args[4]))
        elif args[2] == "-gui":
            print("Initializing GUI...")
            launchGUI(args, name)
        else:
            printUsage()
    else:
        printUsage()

def GUImode():
    print "asd"


def launchGUI(args, name):
    ipArg ="Google.com"
    modeArg = "-ports"
    startArg = "443"
    endArg = "443"

    gui = Tk()
    gui.title(name)
    gui.geometry('450x300+200+200')

    targetLabel = StringVar()
    targetLabel.set("Enter target IP, domain or subnet:")
    targetText = Label(gui, textvariable=targetLabel, height=1, font=23)
    targetText.pack()

    useLabel = StringVar()
    useLabel.set("(Ex: 174.128.244.66  or google.com  or 127.0.0)")
    useText = Label(gui, textvariable=useLabel)
    useText.pack()

    target = StringVar(None)
    targetIp = Entry(gui, textvariable=target)
    targetIp.pack()

    modeText = StringVar()
    modeText.set("Select a mode:")
    modeLabel = Label(gui, textvariable=modeText, height=1)
    modeLabel.pack(pady=10)

    mode = StringVar()
    mode.set(NONE)
    modeRadio = Radiobutton(gui, text='Scan Ports', value='-ports', variable=mode,command=GUImode)
    modeRadio.pack()
    modeRadio = Radiobutton(gui, text='Ping Sub-net', value='-ping', variable=mode, command=GUImode)
    modeRadio.pack()

    rangeText = StringVar()
    rangeText.set("Enter range to scan (Ex: 0 500)")
    rangeLabel = Label(gui, textvariable=rangeText, height=1, pady=10)
    rangeLabel.pack()

    rangeIn = StringVar(None)
    rangeEntry = Entry(gui, textvariable=rangeIn, text="Start")
    rangeEntry.pack()

    inputArgs = [name,ipArg,modeArg,startArg,endArg]


    button = Button(gui, text="Execute", width=20)
    button.pack(side='bottom', padx=15,pady=15)




    gui.mainloop()

def scanPorts(ip, start, end):
    for i in range(start, (end +1)):
        if checkHost(ip, i):
            print("Scan on " + ip + ":" + str(i) + " returned " + "     OPEN")
        else:
            print("Scan on " + ip + ":" + str(i) + " returned " + "     CLOSED")



def printUsage():
    print("USAGE: NewtworkMapper.py <option (-ping or -ports)><subnet> <start> <end>")
    print("Ping Ex: 'NewtworkMapper.py -ping 192.168.0 0 255' \n will ping 192.168.0.0 through 192.168.0.255")
    print(
        "Port scan Ex: 'NewtworkMapper.py -ports 192.168.0.0 0 443' \n will check ports if ports 0 through 443 are open on 192.168.0.0 ")


parseArgs(sys.argv, appName)
