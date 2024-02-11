# Mqtt & Node-red Run on Raspberry pi4
node-red and Mqtt run on localhost || ทั้งหมดรันบนตัว `Raspberry Pi4`
# Inspirational Quotes
[![platform](https://img.shields.io/badge/platform-Node--RED-red)](https://nodered.org)
[![library](https://img.shields.io/badge/library-Paho--MQTT-g)](https://pypi.org/project/paho-mqtt/)
[![protocol](https://img.shields.io/badge/protocol-MQTT--Protocal-purple)](https://mqtt.org/)
[![req](https://img.shields.io/badge/Request-Python--3.7%2B-blue)]()

## Installation && Getting started
```bash
$ sudo apt-get update
$ sudo apt-get upgrade
```
### 1. Node-red
```bast
$ bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)
```
### 2. paho-mqtt
```bash
$ sudo apt-get install python3-paho-mqtt
```
### 3. mosquitto
```bash
$ sudo apt-get install mosquitto mosquitto-clients
```
### Open Server mosquitto || เปิดใช้ Server mosquitto
```bash
$ sudo systemctl enable mosquitto
$ sudo systemctl start mosquitto
```

## Run Locally && Test
Run `Node-red` || สั่งทำงาน `Node-red`
```sudo
$ node-red
```
หลังจากนั้่นให้ลองเข้า ip `localhost:1880` จะมีให้ใส่ `username` & `password` ที่เราตั้งในตอนติดตั้ง `node-red` <br>
**เสริม จะทำก็ได้หรือไม่ทำก็ได้<br>
Run automatically at startup || เปิดอัตโนมัติตอนเปิด Pi
```sudo
$ sudo systemctl enable nodered.service
```
ลอง reboot เพื่อเช็คว่าใช้งานได้ไหม
```sudo
$ sudo reboot
```
