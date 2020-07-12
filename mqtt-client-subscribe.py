# This is code for an MQTT client which subscribes to a topic, i.e., listens for incoming payload
# We also configure the broker's IP address along with username and password
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

time.sleep(15) # wait for incoming payload
client.loop_stop() # stop listening