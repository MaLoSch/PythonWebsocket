import websocket #import websockt library -> pip install websocket-client
import ssl # import ssl library (native)
import json # import json library (native)

def on_message(ws, message): # function which is called whenever a new message comes in
    json_data = json.loads(message) # incoming message is transformed into a JSON object
    print(json_data) # printing the data (for testing purposes)
    print(json_data["blockHash"]) # printing a specific part of the JSON object (for testing purposes)
    print("") # printing new line for better legibility

def on_error(ws, error): # function call when there is an error
    print(error)

def on_close(ws): # function call when the connection is closed (this should not happend currently as we are staying connected)
    print("### closed ###")

def on_open(ws): # function call when a new connection is established
    print("### open ###")

if __name__ == "__main__": # main loop
    websocket.enableTrace(True) # print the connection details (for debugging purposes)
    ws = websocket.WebSocketApp("wss://testnet-explorer.binance.org/ws/block", # websocket URL to connect to
                              on_message = on_message, # what should happen when we receive a new message
                              on_error = on_error, # what should happen when we get an error
                              on_close = on_close) # what should happen when the connection is closed
    ws.on_open = on_open # call on_open function when the ws connection is opened
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE}) # run code forever and disable the requirement of SSL certificates
