import json
import time
import websocket
from concurrent.futures import ThreadPoolExecutor 

class constant:

    guild_id = "id"
    channel_id = "id"
    with open("tokens.txt") as f:
        tokens = [x.strip() for x in f.readlines()] 

class discord:

    def connect(token):
        ws = websocket.WebSocket()
        ws.connect("wss://gateway.discord.gg/?v=9&encoding=json")
        RECV = json.loads(ws.recv())
        heartbeat_interval = RECV['d']['heartbeat_interval']
        ws.send(json.dumps({
                    "op":2,
                    "d": {
                        "token":token, 
                        "properties": {
                            "$os":"windows",
                            "$browser":"Discord",
                            "$device": "desktop" 
                            }
                        }
                    }))
        ws.send(json.dumps({
                    "op":4,
                    "d": {
                        "guild_id":constant.guild_id, 
                        "channel_id": constant.channel_id,
                        "self_mute":True,
                        "self_deaf":True
                    }
                }))
        while True:
            time.sleep(heartbeat_interval/1000)
            try:
                ws.send(json.dumps({
                    "op":1,
                    "d":None}))
            except Exception:
                break

    def online(token):
        ws = websocket.WebSocket()
        ws.connect("wss://gateway.discord.gg/?v=9&encoding=json")
        RECV = json.loads(ws.recv())
        heartbeat_interval = RECV['d']['heartbeat_interval']
        while True:
            time.sleep(heartbeat_interval/1000)
            try:
                ws.send(json.dumps({
                    "op":1,
                    "d":None}))
            except Exception:
                break

    def livestream(token):
        ws = websocket.WebSocket()
        ws.connect("wss://gateway.discord.gg/?v=9&encoding=json")
        RECV = json.loads(ws.recv())
        heartbeat_interval = RECV['d']['heartbeat_interval']
        ws.send(json.dumps({
                    "op":2,
                    "d": {
                        "token":token, 
                        "properties": {
                            "$os":"windows",
                            "$browser":"Discord",
                            "$device": "desktop" 
                            }
                        }
                    }))
        ws.send(json.dumps({
                    "op":4,
                    "d": {
                        "guild_id":constant.guild_id, 
                        "channel_id": constant.channel_id,
                        "self_mute":True,
                        "self_deaf":True
                    }
                }))
        ws.send(json.dumps({
            "op":18,
            "d": {
                "type":"guild",
                "guild_id":constant.guild_id, 
                "channel_id": constant.channel_id,
                "preferred_region":"singapore"
                }
            }))
        while True:
            time.sleep(heartbeat_interval/1000)
            try:
                ws.send(json.dumps({
                    "op":1,
                    "d":None}))
            except Exception:
                break

class function:

    def main(method):
        threads_create = [] 
        print("running ...")
        with ThreadPoolExecutor(max_workers=len(constant.tokens)) as executor:
            if method == "livestream":
                for token in constant.tokens:
                    threads_create.append(executor.submit(discord.livestream,token))
            
            elif method == "online":
                for token in constant.tokens:
                    threads_create.append(executor.submit(discord.online,token))
            
            elif method == "connect":
                for token in constant.tokens:
                    threads_create.append(executor.submit(discord.connect,token))

            else:
                print("invalid")

#function.main("connect")
#function.main("online")
function.main("livestream")