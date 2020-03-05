
from guizero import *
from discord_webhook import DiscordWebhook
import os
import time



myfile = open("Link.txt", "rt")
Link = myfile.read()
myfile.close()

def launch_message_mode():

         def read():
                  myfile = open("Message.txt", "rt")
                  message = myfile.read()
                  myfile.close()
                  
         def save():
                  file = open("Message.txt","w") 
                  file.write(box.value) 
                  file.close()
                  clicked()

         def clicked():
                  myfile = open("Message.txt", "rt")
                  message = myfile.read()
                  myfile.close() 
                  
                  webhook = DiscordWebhook(url=Link, content=message)
                  response = webhook.execute()
                  
                  message = Text(gui, text="Message Sent", size=9)

         guimessage = App(title='DiscordHook | Message Mode | v1.01')
         message = Text(guimessage, text="", size=1)
         message = Text(guimessage, text="DiscordHook - A discord webhook sender", size=15)
         message = Text(guimessage, text="by fortbrleaks", size=11)

         message = Text(guimessage, text="", size=1)
         message = Text(guimessage, text="Message Mode", font='Comic Sans MS', size=15)
         message = Text(guimessage, text="", size=1)

         message = Text(guimessage, text="Link using:", size=13)

         linkbox = TextBox(guimessage, width=50, multiline=True, height=3)
         linkbox.value=Link
         linkbox.after(100, read)

         message = Text(guimessage, text="", size=1)

         message = Text(guimessage, text="Enter message here:", size=13)

         box = TextBox(guimessage, width=50, multiline=True, height=10)
         box.value='Replace this with message text...'
         box.after(100, read)


         message = Text(guimessage, text="", size=10)

         sendmessagebutton = PushButton(guimessage, command=save, text='Send')
         sendmessagebutton.width=5
         sendmessagebutton.height=1

         message = Text(guimessage, text="Log:", font='Arial', size=13)
         guimessage.display()
         

def launch_embed_mode():
         message = Text(guiembed, text="", size=1)
         guiembed = Window(gui, title="Embed Mode")
         message = Text(guiembed, text="DiscordHook - A discord webhook sender", size=15)
         message = Text(guiembed, text="by fortbrleaks", size=11)

         message = Text(guiembed, text="", size=1)
         message = Text(guiembed, text="Embed Mode", font='Comic Sans MS', size=15)
         message = Text(guiembed, text="", size=1)


def credits_function():
         print("Credits")

def github_function():
         gui.info("GitHub Page", "Download updates at: https://www.github.com/thomaskeig/DiscordHook")




# MAIN MENU
gui = App(title='DiscordHook | Main Menu | v1.01')
#gui.info("Welcome", "Thank you for using DiscordHook \n\nYou can support me in the Fortnite Item Shop by using code creator code: FBR \n\nDiscord Server: https://discord.gg/HsqYa5x \n\nClick OK below to begin")

message = Text(gui, text="", size=1)
message = Text(gui, text="DiscordHook - A discord webhook sender", size=15)
message = Text(gui, text="by fortbrleaks", size=11)
message = Text(gui, text="", size=1)
message = Text(gui, text="Main Menu", font='Comic Sans MS', size=15)
message = Text(gui, text="", size=1)
message = Text(gui, text="▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬", size=10)
message = Text(gui, text="", size=1)


openmsgmodebutton = PushButton(gui, command=launch_message_mode, text='Open Message Mode')
openmsgmodebutton.width=15
openmsgmodebutton.height=1

message = Text(gui, text="", size=1)

openembedmodebutton = PushButton(gui, text='COMING SOON: Embed Mode')
openembedmodebutton.width=22
openembedmodebutton.height=1



#menubar = MenuBar(gui,
#                  toplevel=["Modes"],
#                  options=[
#                      [ ["Embed Mode", launch_embed_mode], ["Message Mode", launch_message_mode] ]
#                  ])

gui.display()
