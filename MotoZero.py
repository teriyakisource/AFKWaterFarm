import gpiozero as gz
import time

#port 1
relay = gz.Motor(24, 27)
relay_enable = gz.OutputDevice(5, initial_value=1)

#port 2
prt2 = gz.Motor(6, 22)
prt2_enable = gz.OutputDevice(17, initial_value=1)

#port 3
prt3 = gz.Motor(23, 16)
prt3_enable = gz.OutputDevice(12, initial_value=1)

#port 4
prt4 = gz.Motor(13, 18)
prt4_enable = gz.OutputDevice(25, initial_value=1)

def on(relay):
    relay.forward()

def off(relay):
    relay.stop()

def procedure(relay):
    print("Starting...")
    on(relay)
    print("Pumping...")
    time.sleep(6)
    print("Finishing...")
    off(relay)
    print("Done")
    time.sleep(55)
    

def quickstart(relay, length):
    print("Starting...")
    on(relay)
    print("Pumping...")
    for i in range(length):
        print(length-i)
        time.sleep(1)
    print("Finishing...")
    off(relay)
    print("Done\n")
    time.sleep(1)
    
