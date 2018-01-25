import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

WAIT = 400
BTN_PIN = 12
LED_PIN = 40

btn_on = 0

GPIO.setup(BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)

def light_LED():
    global btn_on

    print('button press!')
    GPIO.output(LED_PIN, GPIO.HIGH)
    btn_on = 1

def dark_LED():
    global btn_on

    print('button release!')
    GPIO.output(LED_PIN, GPIO.LOW)
    btn_on = 0

def btn_handler(pin):
    global btn_on

    if not btn_on:
        light_LED()
    elif btn_on:
        dark_LED()


try:
    GPIO.add_event_detect(BTN_PIN,
                          GPIO.BOTH,
                          callback=btn_handler,
                          bouncetime=WAIT)

    while True:
        pass

except KeyboardInterrupt:
    print('exit')

finally:
    GPIO.cleanup()
