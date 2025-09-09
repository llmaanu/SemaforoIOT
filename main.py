from machine import Pin 
from utime import sleep 

led_amarelo = Pin(14, Pin.OUT)
led_verde = Pin (12, Pin.OUT)
led_vermelho = Pin (15, Pin.OUT)

while True: 
    led_verde.on()
    print("Led Verde Ligado")
    sleep(10)
    led_verde.off()
    print("Led Verde desligado")

    sleep(1)

    led_amarelo.on()
    print("Led amarelo Ligado")
    sleep(10)
    led_amarelo.off()
    print("Led amarelo Desligado")

    sleep(1)

    led_vermelho.on()
    print("Led vermelho Ligado")
    sleep(10)
    led_vermelho.off()
    print("Led Vermelho Desligado")

    sleep(1)


