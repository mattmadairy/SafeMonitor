from gpiozero import Button
from subprocess import check_call
from signal import pause
from eventLog import logging

def reboot():
    event = 'REBOOT CALLED- EXTERNAL RESET BUTTON'
    logging(event)
    check_call(['sudo', 'reboot'])
    
reboot_btn = Button(25, hold_time=3)
reboot_btn.when_held = reboot
pause()
