from gpiozero import LED, Button, Buzzer
from time import sleep
from eventLog import logging
from pushNotification import pushOver

green = LED(23)
red = LED(24)
bz = Buzzer(16)
door = Button(5)

def doorClosed():
    bz.off()
    red.off()
    green.on()
    
def doorOpened(): ### wait for press
    log = 'DOOR OPENED'
    openMessage = 'SAFE DOOR OPENED FOR LONGER THAN x SECONDS!'
    logging(log)
    green.off()
    red.on()
    sleep(5) ### change to 30 or 60 after dev complete
    pushOver(openMessage)

    while door.is_pressed:
        door_open = True
        if door_open == True:
            red.on()
            bz.on()
            sleep(0.2)
            red.off()
            bz.off()
            sleep(0.2)
    
while True:
    if door.is_pressed:
        doorOpened()
    else:
        doorClosed()