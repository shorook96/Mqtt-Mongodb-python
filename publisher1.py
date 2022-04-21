import paho.mqtt.client as mqtt
from random import randrange , uniform
import time
import pymongo as py
clientdb=py.MongoClient("mongodb+srv://iot:iot123@projectcluster.lrysq.mongodb.net/test")
# clientdb=py.MongoClient("mongodb://localhost:27017/")
db= clientdb["publisher1"]
col=db["temperature_inside"]


client = mqtt.Client("temperature_inside")
client.connect("mqtt.eclipseprojects.io")

status=" "
while True:
    randNumber=randrange (12,30)
    client.publish("Temperature",payload=str(randNumber)+","+"temperature_inside")
    
  
    

    if randNumber < 25 and randNumber >18:
        status="perfect temperature"
    elif randNumber<18:
        status="cold"
    else:
        status="hot"
    t=time.ctime()
    col.insert_one({"temperature_inside":randNumber,"status":status,"time":t})
    print(randNumber," time now is ",time.ctime()," ",status)
    time.sleep(3)
    
