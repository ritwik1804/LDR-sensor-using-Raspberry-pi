from gpiozero import LED, LightSensor
from time import sleep

led = LED(14)

ldr = LightSensor(18)

while True:
    ldr_value = ldr.value

    if ldr_value < 0.5:
        led.on()
    else:
        led.off()

    sleep(0.1)
