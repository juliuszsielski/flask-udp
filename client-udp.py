import socketio
import json

sio = socketio.Client()
sio.connect('http://localhost:8000')




# to enable receiving data from server
@sio.event
def message(data_received):
    print('(server) received: ' + data_received)

while True:
    data_send = input("Please enter something: ")
    # data_send = 'aaaa'
    sio.emit('message', data_send)
    print('(client) send: ' + data_send)

# sio.wait()
# sio.disconnect()