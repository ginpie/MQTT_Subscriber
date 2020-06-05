import paho.mqtt.client as mqtt
import time
import csv

SERVER = "comp3310.ddns.net"
PORT = 1883
USERNAME = "students"
PASSWORD = "33106331"
CLIENT_ID="3310-u6743886"
SLOW = ["counter/slow/q0", "counter/slow/q1", "counter/slow/q2"]
FAST = ["counter/fast/q0", "counter/fast/q1", "counter/fast/q2"]
ALL = SLOW + FAST
list = []
previous_time = time.time()


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
   if rc == 0:
      print("Successfully connected with code: " + str(rc))
   else:
      print("Error with code: " + str(rc))


def on_disconnect(clietn, userdata, rc):
   print("client disconnected ok")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
   this_time = time.time()
   global previous_time 
   gap = round((this_time - previous_time) * 1000000)
   previous_time = this_time
   ms = (msg.topic, msg.payload, gap)
   list.append(ms)
   print( msg.topic + " " + str(msg.payload) )

def on_log(client, userdata, level, buf):
   print("log: " + buf )

def on_publish(client, userdata, mid):
   print("on_pub callback mid= ", mid)

# subscribe to one of the topics at a time
for i in range(5,6):
   
   client = mqtt.Client(CLIENT_ID)
   client.on_connect = on_connect
   client.on_message = on_message
   # client.on_log = on_log
   client.username_pw_set(USERNAME, PASSWORD)
   client.connect(SERVER, PORT)

   list.append(("qos", i))
   topic = ALL[i]
   lv = i%3
   client.subscribe(topic, qos=lv)
   client.subscribe("$SYS/#")
   # client.subscribe("studentreport/u6743886/#", 2)

   client.loop_start()
   time.sleep(320)
   client.loop_stop()
   
   client.unsubscribe(topic)
   
client.disconnect()

with open('test.csv', 'w', newline='') as csvfile:
   writ = csv.writer(csvfile)
   for i in range(0, len(list)):
      writ.writerow(list[i])
