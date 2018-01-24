import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GRE_PIN = 12
YEL_PIN = 16
RED_PIN = 18

GPIO.setup(GRE_PIN, GPIO.OUT)
GPIO.setup(YEL_PIN, GPIO.OUT)
GPIO.setup(RED_PIN, GPIO.OUT)

def init():
    GPIO.output(GRE_PIN, GPIO.LOW)
    GPIO.output(YEL_PIN, GPIO.LOW)
    GPIO.output(RED_PIN, GPIO.LOW)
    
def light(pin, duration):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(pin, GPIO.LOW)
    
def main():
    init()
    light(RED_PIN, 4)
    light(GRE_PIN, 4)
    light(YEL_PIN, 2)
    
try:
    while True:
        main()
except KeyboardInterrupt:
    print('Exit')
finally:
    GPIO.cleanup()


