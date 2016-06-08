import sys
import RPi.GPIO as gpio #https://pypi.python.org/pypi/RPi.GPIO
import time

#Variablen ins Programm uebergeben
try: 
    direction = sys.argv[1]
    steps = int(float(sys.argv[2]))
    speed = int(float(sys.argv[3]))
except:
    steps = 0
print ("Keine Perimeter angegeben. Bitte angeben: programmname.py Richtung Schritte Speed")

#Kontrollausgabe der Eingegebenen Perimeter
print("Bewege den Motor %s Schritte nach %s. Speed= %s") % (steps, direction, speed)

#GPIO Vorbereitung
gpio.setmode(gpio.BCM)
#GPIO23 = Dir
#GPIO24 = Step
gpio.setup(23, gpio.OUT)
gpio.setup(24, gpio.OUT)

#Richtung festlegen GPIO = 23
if direction == 'left':
    gpio.output(23, True)
elif direction == 'right':
    gpio.output(23, False)
	
#Schrittzaehler initialisieren
StepCounter = 0

#Geschwindigkeit wird durch eine Wartezeit zwischen den Schritten realisiert
#WaitTime = 0.001
WaitTime = speed

#main
while StepCounter < steps:

    #einmaliger Wechsel zwischen an und aus = Easydriver macht einen Step
    gpio.output(24, True)
    gpio.output(24, False)
    StepCounter += 1

    #wartezeit
    time.sleep(WaitTime)

#GPIO freigeben, damit andere Programme damit arbeiten koennen
gpio.cleanup()

print ("Bewegung beendet.")