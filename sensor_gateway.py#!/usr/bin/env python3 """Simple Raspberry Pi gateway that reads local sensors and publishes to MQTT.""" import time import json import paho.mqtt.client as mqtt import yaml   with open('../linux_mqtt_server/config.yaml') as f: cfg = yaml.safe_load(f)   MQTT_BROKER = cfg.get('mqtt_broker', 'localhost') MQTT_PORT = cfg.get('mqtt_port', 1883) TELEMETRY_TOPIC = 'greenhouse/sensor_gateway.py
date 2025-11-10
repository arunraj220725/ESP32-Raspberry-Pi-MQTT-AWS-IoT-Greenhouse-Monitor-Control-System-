#!/usr/bin/env python3
"""Simple Raspberry Pi gateway that reads local sensors and publishes to MQTT."""
import time
import json
import paho.mqtt.client as mqtt
import yaml


with open('../linux_mqtt_server/config.yaml') as f:
cfg = yaml.safe_load(f)


MQTT_BROKER = cfg.get('mqtt_broker', 'localhost')
MQTT_PORT = cfg.get('mqtt_port', 1883)
TELEMETRY_TOPIC = 'greenhouse/telemetry'


client = mqtt.Client('rpi-gateway')
client.connect(MQTT_BROKER, MQTT_PORT, 60)


def read_temp():
# Replace with actual sensor read (DS18B20, DHT22, etc.)
return 25.0


def main():
while True:
t = read_temp()
payload = {
'node': 'rpi-gateway',
'temperature': t,
'ts': int(time.time())
}
client.publish(TELEMETRY_TOPIC, json.dumps(payload))
time.sleep(5)


if __name__ == '__main__':
main()
