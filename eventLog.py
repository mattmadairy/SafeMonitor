### Logging module
from time import ctime
from datetime import date


def logging(event):
    fileName = ('/home/pi/Documents/SafeMonitor/logfiles/'
    + str(date.today()) + '_logfile.txt')
    
    f = open(fileName, 'a')
    f.write(ctime() + ': ' + event + '\n')
    f.close()