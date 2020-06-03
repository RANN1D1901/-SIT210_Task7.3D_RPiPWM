import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 4
ECHO = 18
led=17
buzz=21
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.setup(led,GPIO.OUT)
GPIO.setup(buzz,GPIO.OUT)
p=GPIO.PWM(led,50)
p1=GPIO.PWM(buzz,50)
p.start(30)
p1.start(30)
def Distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == False:
        start = time.time()

    while GPIO.input(ECHO) == True:
        end = time.time()

    sig_time = end-start

    #CM:
    distance = sig_time / 0.000058
    return distance
while 1:

    distance=Distance()
    print('Distance: {} centimeters'.format(distance))

    if(distance>=50):
        p.ChangeDutyCycle(0)
        p1.ChangeDutyCycle(0)
        time.sleep(0.02)
        
    if(distance<50 and distance>=30):
        p.ChangeDutyCycle(5)
        p1.ChangeDutyCycle(5)
        time.sleep(0.02)
    if(distance<30 and distance>=20):
        p.ChangeDutyCycle(10)
        p1.ChangeDutyCycle(10)
        time.sleep(0.02)
    if (distance<20 and distance>=10):
        p.ChangeDutyCycle(70)
        p1.ChangeDutyCycle(70)
        time.sleep(0.02)
    if(distance<10):
        p.ChangeDutyCycle(100)
        p1.ChangeDutyCycle(100)
        time.sleep(0.02)

p1.stop()
p.stop()
GPIO.cleanup()
