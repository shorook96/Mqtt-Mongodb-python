import paho.mqtt.client as mqtt
from random import randrange , uniform
import time 
import pymongo as py
clientdb=py.MongoClient("mongodb+srv://iot:iot123@projectcluster.lrysq.mongodb.net/test")
# clientdb=py.MongoClient("mongodb://localhost:27017/")
db= clientdb["publisher2"]
col=db["temperature_outside"]

client = mqtt.Client("temperature_outside")
client.connect("mqtt.eclipseprojects.io")


while True:
    randNumber=randrange (5,50)
    client.publish("Temperature",payload=str(randNumber)+","+"temperature_outside")
    if randNumber < 33 and randNumber >16:
        status="perfect temperature"
    elif randNumber<16:
        status="cold"
    else:
        status="hot"
    t=time.ctime()
    col.insert_one({"temperature_outside":randNumber,"status":status,"time":t})

    print(randNumber," time now is ",time.ctime()," ",status)
    time.sleep(5)
    
