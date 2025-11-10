import paho.mqtt.client as mqtt
import json

BROKER = '0.0.0.0'
PORT = 1883
TOPIC = 'greenhouse/telemetry'


def on_connect(client, userdata, flags, rc):
print('connected with rc', rc)
client.subscribe(TOPIC)


def on_message(client, userdata, msg):
try:
payload = msg.payload.decode('utf-8')
data = json.loads(payload)
print('telemetry:', data)
except Exception as e:
print('failed to parse message', e)


client = mqtt.Client('mqtt-service')
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, PORT, 60)
client.loop_forever()
