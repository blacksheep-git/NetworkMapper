# NetworkMapper
This program takes in command line input for:
- Target IP/Subnet/Domain
- Operating mode (-ping or -ports)
- Range of subnet hosts to ping or ports to scan

# Usage
     $ python2 NewtworkMapper.py <subnet or IP> <option (-ping or -ports)> <starting port/host> <ending port/host>

     Ping Ex: 'python2 NewtworkMapper.py 192.168.0 -ping 1 255'
     will ping 192.168.0.1 through 192.168.0.255

     Port scan Ex: 'python2 NewtworkMapper.py 192.168.0.0 0 -ports 442 443'
     will check if ports 443 through 443 are open on 192.168.0.0


# Port Scan Example:

     $ python2 NetworkMapper.py google.com -ports 440 450
     Checking google.com on ports 440 through 450...
     Scan on google.com:440 returned      CLOSED
     Scan on google.com:441 returned      CLOSED  
     Scan on google.com:442 returned      CLOSED
     Scan on google.com:443 returned      OPEN
     Scan on google.com:444 returned      CLOSED
     Scan on google.com:445 returned      CLOSED
     Scan on google.com:446 returned      CLOSED
     Scan on google.com:447 returned      CLOSED
     Scan on google.com:448 returned      CLOSED
     Scan on google.com:449 returned      CLOSED
     Scan on google.com:450 returned      CLOSED



# Ping sweep example: 

     $ python2 NetworkMapper.py 216.128.235 -ping 28 34

     Pinging IP's from 216.128.235.28 to 216.128.235.34...


     Ping to 216.128.235.28    SUCCESS
     Ping to 216.128.235.29    FAIL
     Ping to 216.128.235.30    SUCCESS
     Ping to 216.128.235.31    SUCCESS
     Ping to 216.128.235.32    SUCCESS
     Ping to 216.128.235.33    FAIL
     Ping to 216.128.235.34    SUCCESS

# GUI Supported
To use the GUI, uncomment the Tkinter imports (line 5 and 6) at the top of the NetworkMapper.py. Make sure you have installed Tkinter packages.

# GUI Example
     $ python2 NetworkMapper.py 216.128.235 -gui
     Initializing GUI...



