import paho.mqtt.client as mqtt

BROKER = "0.0.0.0"
PORT = 1883

def on_message(client, userdata, msg):
    print(f"{msg.topic} → {msg.payload.decode()}")

client = mqtt.Client()
client.on_message = on_message
client.connect(BROKER, PORT)
client.subscribe("greenhouse/#")
client.loop_forever()
