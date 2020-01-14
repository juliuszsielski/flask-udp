from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
                    
@app.route('/')
def index():
    return render_template('index.html')

# @socketio.on('aaa')
# def test_connect():
#     print("Welcome, aaa received")
#     emit('aaa_response', {'data': 'Server'})

@socketio.on('message')
def handle_message(message):
    print('(server) received: ' + message)
    socketio.emit('message', message)

@socketio.on('connect')
def connect():
    print('(server): client connected')
    # emit('my response', {'data': 'Connected'})

@socketio.on('disconnect')
def disconnect():
    print('(server): client disconnected')

    
if __name__ == '__main__':
    socketio.run(app, port=8000)