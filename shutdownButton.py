from gpiozero import Button
from subprocess import check_call
from signal import pause
from eventLog import logging

shutdownMes = 'SHUTDOWN CALLED - EXTERNAL RESET BUTTON'
def shutdown():
    logging(shutdownMes)
    check_call(['sudo', 'shutdown'])

shutdown_btn = Button(25, hold_time=4)
shutdown_btn.when_held = shutdown
pause()