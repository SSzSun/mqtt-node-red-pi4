import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

LED_PIN = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

def on_connect(client, userdata, flags, rc):
    client.subscribe("rasp/v_s")
    if rc == 0:
        client.publish("pi/status", 1)
        print("Connected successfully\n==================")
    else:
        client.publish("pi/status", 3)
        print("Connection failed with code", rc)

def on_message(client, userdata, msg):
    received_data = msg.payload
    decoded_data = received_data.decode('utf-8')

    print(f'Server sand : {decoded_data}\n')
    if decoded_data == '1':
        print(f'Buys')
    elif decoded_data == '5':
        client.publish("pi/status", 3)
        client.disconnect()
    else:
        print(f'Enter Else\n---------')
        client.publish("status/wait", 2)
        time.sleep(3)
        print(f'Befor-loop\n---------')
        gpio_loop(5)
        print(f'After-loop\n---------')
        client.publish("pi/status", 1)
        print(f'After-publish\n---------')

def gpio_loop(x):
    for _ in range(x):
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.5)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

client.loop_forever()
