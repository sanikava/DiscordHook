
from guizero import *
from discord_webhook import DiscordWebhook
import os
import time

def clicked():

         myfile = open("Message.txt", "rt")
         message = myfile.read()
         myfile.close() 
         
         webhook = DiscordWebhook(url=Link, content=message)
         response = webhook.execute()
         
         message = Text(gui, text="Message Sent", size=13)

myfile = open("Link.txt", "rt")
Link = myfile.read()
myfile.close()


def read():
         myfile = open("Message.txt", "rt")
         message = myfile.read()
         myfile.close()
         
def save():
         file = open("Message.txt","w") 
 
         file.write(box.value) 
 
         file.close()

         clicked()





gui = App(title='DiscordHook | v1.00') # Window title

gui.info("Welcome", "Thank you for using DiscordHook \n\nYou can support me in the Fortnite Item Shop by using code creator code: FBR \n\nDiscord Server: https://discord.gg/HsqYa5x \n\nClick OK below to begin")
#Info box

message = Text(gui, text="DiscordHook - A discord webhook sender", size=15)
message = Text(gui, text="by fortbrleaks", size=11)

message = Text(gui, text="", size=1)

message = Text(gui, text="Enter message here:", size=13)

box = TextBox(gui, width=50, multiline=True, height=10)
box.value='Replace this with message text...'
box.after(100, read)


message = Text(gui, text="", size=10)

button = PushButton(gui, command=save, text='Send')
button.width=5
button.height=1

message = Text(gui, text="Log:", font='Arial', size=13)

print("Launched GUI")
gui.display()
