# This is code for an MQTT client which publishes a payload to a topic
# We also configure the broker's IP address along with username and password
import paho.mqtt.client as mqtt

broker = "{Broker IP Address}" 
username = "{MQTT Client Username}"
password = "{MQTT Client Password}"

# Create new MQTT instance,
client = mqtt.Client(client_id="")  # Client ID is used to tag the requests from broker side
# Enter MQTT client credentials, this is configured on the broker,
client.username_pw_set(username, password) 
# Connect to broker address, default port is 1833,
client.connect(broker) 

# Publish payload to a topic 
publish_topic = "{MQTT TOPIC}" # example: "/Platform_A/Instance_1/Object_X/Property_X"
# Some value like, JSON, int, float, etc.
payload = "{some value}" # example: '{"COMMAND": false}' or 100
# Publish payload to broker, retain=True means that the previous value is persistent
client.publish(publish_topic, payload, retain=True) 

