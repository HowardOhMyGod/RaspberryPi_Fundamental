import RPi.GPIO as GPIO
import time

buzzer_pin = 38
led_pin = 40

GPIO.setmode(GPIO.BOARD)
GPIO.setup(buzzer_pin, GPIO.OUT)
GPIO.setup(led_pin, GPIO.OUT)

def buzz(pitch, duration):
    period = 1.0 / pitch
    half_period = period / 2
    cycles = int(duration * pitch)
    for i in range(cycles) :
        GPIO.output(buzzer_pin, GPIO.HIGH)
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(half_period)
        GPIO.output(buzzer_pin, GPIO.LOW)
        time.sleep(half_period)
        GPIO.output(led_pin, GPIO.LOW)
try:
    while True :
        pitch_s = input("Enter Pitch (200 to 2000): ")
        duration_s = input("Enter Duration (seconde): ")
        buzz(float(pitch_s), float(duration_s))

except KeyboardInterrupt:
    print("Exception: KeyboardInterrupt")

finally:
    GPIO.cleanup()