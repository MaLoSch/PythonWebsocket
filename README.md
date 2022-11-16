# PythonWebsocket
Simple python script which connects to an publicly available websocket server on https://testnet-explorer.binance.org/

## Setup
The script needs the following libraries
- websocket (https://websocket-client.readthedocs.io)
- ssl
- json

ssl and json are installed by default. To install websocket run _pip install websocket-client_.

## Output
The script simply converts the incoming datat to JSON and then prints the data to the terminal. Once the full JSON and once a selection. It does so indefinitely – meaning you need to come up with your own logic to stop the connection.
