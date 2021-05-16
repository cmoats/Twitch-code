#!/usr/bin/env python3
import socket
import keyboard
import simulate_key as sim

host='irc.chat.twitch.tv' #this is where twitch link is at
port= 6667   #this might be 80 idk
channel='ludwig' #the channel you want to join in lowercase letters

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

oauth = '' #need to go to twitch irc documentation to request
nick = 'shabooya12' #your twitch username goes here in undercase letters

#sends our password and username to connect to irc 
s.sendall(f" PASS {oauth}\n".encode("utf-8"))
s.sendall(f"NICK {nick}\n".encode("utf-8"))
s.sendall(f"JOIN #{channel}\n".encode("utf-8"))

lulw_count = 0
message_count = 0

while True:
    
    #stops execution of code if escaped is pressed
    if keyboard.is_pressed('esc') == True:
        break

    message=s.recv(2048).decode("utf-8")

    if message[:4]== "PING":
        s.sendall(b"PONG :tmi.twitch.tv\n")
    else:
        splitmsg= message.split(":",2) #we only expect two colons
        try:
            newmsg = splitmsg[2]
            newmsg = newmsg.lower().strip()
            sim.main(newmsg)
        except:
            continue

        print(newmsg)

        #lulw_count += newmsg.lower().count('lulw')
        #lulw_count += 1 if newmsg.lower().count('lulw') > 0 else 0
        #message_count += 1
        #pct = lulw_count / message_count * 100
        #print(f'Message count: {message_count}\t\tLULW Message Percentage: {pct:.2f}%')
