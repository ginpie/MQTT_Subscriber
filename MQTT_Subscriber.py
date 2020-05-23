import paho.mqtt.client as mqtt

SERVER = "comp3310.ddns.net"
PORT: 1883
USERNAME: "students"
PASSWORD: "33106331"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
   print("Connected with code: " + str(rc))
   
   # Subscribing in on_connect() means that if we lose the connection and
   # reconnect then subscriptions will be renewed.
   client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
   print( msg.topic + " " + str(msg.payload) )


client = mqtt.client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(SERVER, PORT, 60)
client.username_pw_set(USERNAME, PASSWORD)

client.loop_forever()