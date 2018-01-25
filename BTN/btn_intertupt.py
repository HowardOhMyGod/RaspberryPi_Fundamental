import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

WAIT = 200
BTN_PIN = 12
GPIO.setup(BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def btn_handler(pin):
    print('button press! pin: ', pin)
    
    
try:
    GPIO.add_event_detect(BTN_PIN,
                          GPIO.FALLING,
                          callback=btn_handler,
                          bouncetime=WAIT)
    while True:
        pass
except KeyboardInterrupt:
    print('exit')
    
finally:
    GPIO.cleanup()
