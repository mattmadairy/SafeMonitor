from gpiozero import Button
from subprocess import check_call
from signal import pause

def shutdown():
    check_call(['sudo', 'shutdown'])

shutdown_btn = Button(25, hold_time=4)
shutdown_btn.when_held = shutdown
pause()