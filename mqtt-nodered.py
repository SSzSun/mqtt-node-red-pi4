
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time
LED_PIN = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("rasp/v_s")

def on_message(client, userdata, msg):

    received_data = msg.payload
    decoded_data = received_data.decode('utf-8')

    # print(msg.topic+" = "+str(msg.payload))
    # print(msg.topic+" = "+decoded_data)
    # print(type(msg.payload))

    # if decoded_data == '10' or decoded_data.isdigit(): 
    print(f'Server sand : {decoded_data}')
    if decoded_data == '10':
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("LED ON")
    elif decoded_data == '5' :
        GPIO.output(LED_PIN, GPIO.LOW)
        print("LED OFF")
    else:
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED_PIN, GPIO.LOW)
        print("Null")
        client.publish("pi/s_v", "error")
    print(f'Server staby')
        
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

client.loop_forever()