import RPi.GPIO as GPIO
import time

# GPIO setting
GPIO.setmode(GPIO.BOARD)

GPIO_NO = 8
GPIO.setup(GPIO_NO, GPIO.OUT, initial=GPIO.LOW)

try:
    for i in range(1, 100):
        if i % 2 == 0:
            GPIO.output(GPIO_NO, GPIO.HIGH)
        else:
            GPIO.output(GPIO_NO, GPIO.LOW)
        time.sleep(1)
         
except KeyboardInterrupt:
    pass

GPIO.cleanup()
