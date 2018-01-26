import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

BTN_PIN = 12
GPIO.setup(BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

x = 1
print(x)

# This line will block until button was pressed
GPIO.wait_for_edge(BTN_PIN, GPIO.FALLING)


x += 1
print(x)