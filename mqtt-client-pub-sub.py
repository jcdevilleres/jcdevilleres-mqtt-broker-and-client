import paho.mqtt.client as mqtt 
import time

# Callback function when payload received, this is display incoming payload
########################################
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
########################################

broker = "{Broker IP Address}" 
username = "{MQTT Client Username}"
password = "{MQTT Client Password}"

# Create new MQTT instance,
client = mqtt.Client(client_id="")  # Client ID is used to tag the requests from broker side
# Enter MQTT client credentials, this is configured on the broker.
client.username_pw_set(username, password)
# Callbacks to on_message() when payload is received from broker
client.on_message=on_message 

# Connect to broker address, default port is 1833,
client.connect(broker) 
# Start the loop
client.loop_start() 

# Subscribes to a topic, i.e., listen for payloads or messages on the specified topic
subscribe_topic = "{MQTT TOPIC}" # example: "/Platform_A/Instance_1/Object_X/Property_X"

client.subscribe(subscribe_topic) 
# Note: You can also subscribe to multiple topics by calling passing a multiple objects to the function e.g., client.subscribe([({topic_1}, 0), ({topic_2}, 0)])

# Publish payload to a topic 
publish_topic = "{MQTT TOPIC}" # example: "/Platform_A/Instance_1/Object_X/Property_X"
# Some value like, JSON, int, float, etc.
payload = "{some value}" # example: '{"COMMAND": false}' or 100
# Publish payload to broker, retain=True means that the previous value is persistent
client.publish(publish_topic, payload, retain=True) 

time.sleep(15) # Wait for incoming payload
client.loop_stop() # Stop listening