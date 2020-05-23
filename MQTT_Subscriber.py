import paho.mqtt.client as mqtt
import time

SERVER = "comp3310.ddns.net"
PORT = 1883
USERNAME = "students"
PASSWORD = "33106331"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
   if rc == 0:
      print("Successfully connected with code: " + str(rc))
   else:
      print("Error with code: " + str(rc))
   # Subscribing in on_connect() means that if we lose the connection and
   # reconnect then subscriptions will be renewed.
   client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
   print( msg.topic + " " + str(msg.payload) )

def on_log(client, userdata, level, buf):
   print("log: " + buf)

client = mqtt.Client(client_id="3310-u6743886")

client.on_connect = on_connect
client.on_message = on_message
client.on_log = on_log

client.username_pw_set(USERNAME, PASSWORD)
client.connect(SERVER, PORT, 60)

client.subscribe("counter/slow", 0)

time.sleep(0)
# client.disconnect
client.loop_forever()

