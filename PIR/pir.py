import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

pir_pin = 32
GPIO.setup(pir_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def motion_detect(pin):
    print('Motion Detect!')

try:
    GPIO.add_event_detect(pir_pin,
                          GPIO.RISING,
                          callback=motion_detect,
                          bouncetime=200)
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print('exit')

finally:
    GPIO.cleanup()
