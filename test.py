import websocket

# websocket.enableTrace(True)
ws = websocket.WebSocket()
ws.connect("ws://209.126.82.146:8080/")
print(ws.recv_data())
ws.close()