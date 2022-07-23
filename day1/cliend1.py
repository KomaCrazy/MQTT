import paho.mqtt.client as mqtt

Nnode = input("Enter your name : ")
mqttTopic = input("Enter your Topic :")

host = "broker.emqx.io" ; port = 8000

client = mqtt.Client()
client.connect(host)
client.publish(mqttTopic,Nnode+" Connect!")

box = True
while (box) :
    text1 = input("Enter : ")
    if text1 == "Exit" :
        client.publish(mqttTopic,Nnode+"Disconnecd.")  #Topic
        recon = False
    else :
         client.publish(mqttTopic,Nnode + " : " + text1)