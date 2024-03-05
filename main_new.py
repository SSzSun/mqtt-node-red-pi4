import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time
import json
import threading
import sys

LED_PIN = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)


def image_processing(ripeness_level = None):
    if ripeness_level == None:
        return None
    else:
        print(ripeness_level)

def on_connect(client, userdata, flags, rc):
    client.subscribe("ui/contorl")
    client.subscribe("user/input")
    if rc == 0:
        client.publish("sys_nano/status", 1)
        print("======================\nConnected successfully\n======================")
    else:
        client.publish("sys_nano/status", 3)
        print("Connection failed with code", rc)

def on_message(client, userdata, msg):
    received_data = msg.payload
    json_data = json.loads(received_data)
    #print(f'Server sand : {json_data} Type: {type(json_data)}\n')
    ch = json_data['ripeness']

    client.publish("js/outp", json_data['ripeness'])
    if ch == 'q' :
        print('Received "q". Stopping the program.')
        client.publish("sys_nano/status", 3)
        GPIO.cleanup()
        client.disconnect()
        # sys.exit()
    if 'ripeness' in json_data:
        client.publish("sys_nano/status", 2)
        ripeness_level = None
        ripeness = json_data['ripeness']
        if ripeness == 1:
            ripeness_level = 'Unripe' 
        elif ripeness == 2:
            ripeness_level = 'SmallRipe' 
        elif ripeness == 3:
            ripeness_level = 'MediumRipe' 
        elif ripeness == 4:
            ripeness_level = 'Ripe' 
        elif ripeness == 5:
            ripeness_level = 'FullRipe' 
        else:
            print('unknow input')
            

        if ripeness_level is not None:
            result = image_processing(ripeness_level)

        #threading.Thread(target=gpio_loop_and_sleep).start()
    else :
        client.publish("sys_nano/status", 1)

def gpio_loop_and_sleep():
    GPIO.output(LED_PIN, GPIO.HIGH)
    print('Naja')
    time.sleep(5)
    GPIO.output(LED_PIN, GPIO.LOW)
    client.publish("sys_nano/status", 1)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
# client.loop_forever()

client.loop_start()

try:
    while True:
        time.sleep(1)
    
except KeyboardInterrupt:
    GPIO.cleanup()
    client.disconnect()
    sys.exit()