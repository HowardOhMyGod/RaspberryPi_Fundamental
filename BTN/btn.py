import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

WAIT = 0.2
BTN_PIN = 12
GPIO.setup(BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pre_status = None
pretime = time.time()
ctime = None

press_count = 0

try:
    while True:
        input = GPIO.input(BTN_PIN)
        ctime = time.time()
        
        if (input == GPIO.LOW and pre_status == GPIO.HIGH
            and (ctime - pretime) > WAIT):
            pretime = ctime
            press_count += 1
            print('Button Pressed @ ', time.ctime())
            print('count: ', press_count)
        
        pre_status = input
        
except KeyboardInterrupt:
    print('exit')
    
finally:
    GPIO.cleanup()