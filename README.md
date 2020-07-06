# NetworkMapper
This program takes in command line input for:
- Target IP/Subnet/Domain
- Operating mode (-ping or -ports)
- Range of subnet hosts to ping or ports to scan

Port Scan Example:
host $ python2 NetworkMapper.py google.com -ports 440 450
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

Ping sweep example: $ python2 NetworkMapper.py 216.128.235 -ping 1 34
Pinging IP's from 216.128.235.1 to 216.128.235.34...

Ping to 216.128.235.1    SUCCESS
Ping to 216.128.235.2    SUCCESS
Ping to 216.128.235.3    SUCCESS
Ping to 216.128.235.4    SUCCESS
Ping to 216.128.235.5    SUCCESS
Ping to 216.128.235.6    SUCCESS
Ping to 216.128.235.7    SUCCESS
Ping to 216.128.235.8    SUCCESS
Ping to 216.128.235.9    SUCCESS
Ping to 216.128.235.10    SUCCESS
Ping to 216.128.235.11    SUCCESS
Ping to 216.128.235.12    SUCCESS
Ping to 216.128.235.13    SUCCESS
Ping to 216.128.235.14    SUCCESS
Ping to 216.128.235.15    SUCCESS
Ping to 216.128.235.16    SUCCESS
Ping to 216.128.235.17    SUCCESS
Ping to 216.128.235.18    SUCCESS
Ping to 216.128.235.19    SUCCESS
Ping to 216.128.235.20    SUCCESS
Ping to 216.128.235.21    SUCCESS
Ping to 216.128.235.22    SUCCESS
Ping to 216.128.235.23    SUCCESS
Ping to 216.128.235.24    SUCCESS
Ping to 216.128.235.25    SUCCESS
Ping to 216.128.235.26    SUCCESS
Ping to 216.128.235.27    SUCCESS
Ping to 216.128.235.28    SUCCESS
Ping to 216.128.235.29    FAIL
Ping to 216.128.235.30    SUCCESS
Ping to 216.128.235.31    SUCCESS
Ping to 216.128.235.32    SUCCESS
Ping to 216.128.235.33    FAIL
Ping to 216.128.235.34    SUCCESS
