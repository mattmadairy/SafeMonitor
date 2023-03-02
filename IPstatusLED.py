import subprocess as sp
from gpiozero import LED
from time import sleep
from eventLog import logging
### ip addresses - GLOBAL
WAN = '1.1.1.1'
LAN = '10.0.0.1'

### GPIO Pin Numbers - GLOBAL
BLUE = LED(11)
RED = LED(10)
GREEN = LED(9)

def main():
    while True:
        ping(WAN)
        ping(LAN)
        if ping(WAN) == 1 and ping(LAN) == 1:
            RED.off()
            GREEN.off()
            BLUE.on()
        elif ping(WAN) == 0 and ping(LAN) == 1:
            BLUE.off()
            RED.off()
            GREEN.on()
            log = 'WAN LINK DOWN'
            logging(log)
        else:
            BLUE.off()
            GREEN.off()
            RED.on()
            log = 'WAN AND LAN LINK DOWN'
            logging(log)
        sleep(30) ### 30 seconds between pings

def ping(ip):
    status, result = sp.getstatusoutput('ping -c 3 ' + ip)
    
    if status == 0:
        statusip = 1
    
    else:
        statusip = 0
    
    return statusip

main()

### McDoogs 02/24/2023