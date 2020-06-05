import paho.mqtt.client as mqtt
import time
import csv

SERVER = "comp3310.ddns.net"
PORT = 1883
USERNAME = "students"
PASSWORD = "33106331"
CLIENT_ID="3310-u6743886"
TOPICS1 = ["studentreport/u6743886/language", "studentreport/u6743886/network", 
         "studentreport/u6743886/location" ]
TOPICS2 = ["recv", "loss", "dupe", "ooo", "gap", "gvar"]

SPEED = ["slow", "fast"]

MSG1 = ["python, paho-mqtt", "Wifi, 56Mbps downstream, 300ms ping to comp3310.ddns.net", "Franklin, ACT"]
MSG2 = [["1", "0%", "0%", "0%", "997 ms", "86 ms"], 
         ["1", "0%", "0%", "0%", "999 ms", "88 ms"], 
         ["1", "0%", "0%", "0%", "1006 ms", "94 ms"],
         ["93.3", "0%", "0%", "0%", "10.7 ms", "86 ms"], 
         ["23.4", "74.7%", "0%", "0%", "10.6 ms", "48 ms"], 
         ["11.6", "87.2%", "0%", "0%", "10.3 ms", "43 ms"]]


# The callback for when the client receives a CONNACK response from the broker.
def on_connect(client, userdata, flags, rc):
   if rc == 0:
      print("Successfully connected with code: " + str(rc))
   else:
      print("Error with code: " + str(rc))

def on_disconnect(clietn, userdata, rc):
   print("client disconnected ok")

# The callback for when a PUBLISH message is received from the broker.
def on_message(client, userdata, msg):
   print( msg.topic + " " + str(msg.payload) )

def on_log(client, userdata, level, buf):
   print("log: " + buf )

# The callback for publish a message to the broker
def on_publish(client, userdata, mid):
   print("message published: ", mid)

client = mqtt.Client(CLIENT_ID)
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.on_disconnect = on_disconnect
client.on_log = on_log
client.username_pw_set(USERNAME, PASSWORD)
client.connect(SERVER, PORT)


# publish to one topic at a time
for i in range(0, 3):
   
   topic = TOPICS1[i]
   ms = MSG1[i]
  
   # time.sleep(1)
   ret = client.publish(topic, payload=ms, qos=0, retain=True)
   # time.sleep(2)
   print(ret)

   

for s in range(0,2):
   for q in range(0, 3):
      for t in range(0, 6):
         topic = "studentreport/u6743886/" + SPEED[s] + "/" + str(q) + "/" + TOPICS2[t]
         ms = MSG2[s * 3 + q][t]
         
         client.publish(topic, payload=ms, qos=0, retain=True)
         time.sleep(1)

client.disconnect()
