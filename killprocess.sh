### kills all processes related to SafeMonitor
#cd SafeMonitor
#./killprocess.sh >enter
pkill doorStatus.py
pkill IPstatusLED.py
pkill rebootButton.py
python3 off.py