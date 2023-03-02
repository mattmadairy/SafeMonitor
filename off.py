### prototype tool to turn off all output devices
from gpiozero import LED, Buzzer

green = LED(23)
red = LED(24)
blue = LED(12)
bz = Buzzer(16)
GREEN = LED(10)
RED = LED(9)
BLUE = LED(11)

green.off()
red.off()
blue.off()
bz.off()
GREEN.off()
RED.off()
BLUE.off()
