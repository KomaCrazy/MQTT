from tools import *

def on_connect(self, cliend, userdata, rc) :   
    self.subscribe(mqttTopic)
    print('Ready')

def on_message(cliend, userdata,msg):
    sh = msg.payload.decode("utf-8","strict")
    subsh = sh.endswith("google")
    if subsh == True :
       webbrowser.open("https://google.com")

    print(msg.payload.decode("utf-8","strict"))
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(host)
client.loop_forever()