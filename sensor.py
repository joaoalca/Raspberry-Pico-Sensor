from machine import Pin
import utime
gatilho = Pin(21, Pin.OUT)
eco = Pin(20, Pin.IN)
while True:
    gatilho.low()
    utime.sleep_us(2)
    gatilho.high()
    utime.sleep_us(10)
    gatilho.low()
    while eco.value() == 0:
        sinal_desligado = utime.ticks_us()
    while eco.value() == 1:
        sinal_ligado = utime.ticks_us()
    tempo_passado = sinal_ligado - sinal_desligado
    distancia = (tempo_passado * 0.0343) / 2
    print("A distância do objeto é ", distancia, "cm")
    utime.sleep(1)