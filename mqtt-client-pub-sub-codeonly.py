import paho.mqtt.client as mqtt 
import time

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)

broker = "{Broker IP Address}" 
username = "{MQTT Client Username}"
password = "{MQTT Client Password}"

client = mqtt.Client(client_id="")
client.username_pw_set(username, password)
client.on_message=on_message 

client.connect(broker) 
client.loop_start() 

# Subscribe
subscribe_topic = "{MQTT TOPIC}" 
client.subscribe(subscribe_topic) 

# Publish
publish_topic = "{MQTT TOPIC}"
payload = "{some value}"
client.publish(publish_topic, payload, retain=True) 

time.sleep(15)
client.loop_stop()