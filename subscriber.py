import paho.mqtt.client as mqtt
import time 
import pymongo as py
clientdb=py.MongoClient("mongodb+srv://iot:iot123@projectcluster.lrysq.mongodb.net/test")
# clientdb=py.MongoClient("mongodb://localhost:27017/")
db= clientdb["smartphone"]
col=db["temperature"]

def on_message(client,userdata,message):
    info=message.payload.decode("utf-8").split(",")
    print(info)
    col.insert_one({"temperature":info[0],"sender":info[1]})
    
client = mqtt.Client("smartphone")
client.connect("mqtt.eclipseprojects.io")

client.loop_start()
client.subscribe("Temperature")
client.on_message=on_message
time.sleep(60)
client.loop_stop()
