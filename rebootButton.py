from gpiozero import Button, LED
from subprocess import check_call
from signal import pause
from eventLog import logging
from pushNotification import pushOver

rebootMes = 'SafeMonitor manually rebooted'
event = 'REBOOT CALLED- EXTERNAL RESET BUTTON'
blue = LED(12)

def reboot():   
    logging(event)
    pushOver(rebootMes)
    blue.blink(on_time=0.2, off_time=0.2, n=3)
    check_call(['sudo', 'reboot'])
    
reboot_btn = Button(25, hold_time=3)
reboot_btn.when_held = reboot
pause()
