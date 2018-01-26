import RPi.GPIO as GPIO

class LedControler:
    led_pin = 40
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.led_pin, GPIO.OUT)
        GPIO.output(self.led_pin, GPIO.LOW)

    def open(self):
        GPIO.output(self.led_pin, GPIO.HIGH)

    def close(self):
        GPIO.output(self.led_pin, GPIO.LOW)

    def clear(self):
        GPIO.cleanup(self.led_pin)

LED = LedControler()