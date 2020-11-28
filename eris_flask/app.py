from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send
from eris_app.game import Game
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

#new_game = Game(game_level=3)

munchkin = Game(game_level=3) # sets up deck 
player_names = ['ping', 'james', 'abdul'] # this list could be generated however we like
munchkin.setup_players(player_names) # sets up players and draws initial cards from the deck
# @app.route('/')
# def index():
#     return {"data":"hello world"}

# @socketio.on('FromFlask', namespace='/test')
# def test_message(message):
#     emit('my response', {'data': message['data']})

# @app.route('/test')
# @socketio.on('my broadcast event', namespace='/test')
# def test_message(message):
#     emit('my response', {'data': message['data']}, broadcast=True)
# @app.route('/')
# @socketio.on('connection')
# def test_connect():
#     emit('connection', {'data': 'Connected'})
#     print("Client connected")
#     return {"data":"hello world"}

# @app.route('/disconnect')
# @socketio.on('disconnect')
# def test_disconnect():
#     print('Client disconnected')


message_history = {}
message_counter = 0


@socketio.on("message_history")
def handleMessageHistory():
    print(message_history)
    #send(json.dumps(message_history), broadcast=True)
    return json.dumps(message_history)

@socketio.on("new_message")
def handleNewMessage(message_recieved):
    global message_counter
    print(message_recieved)
    message_history[message_counter]=message_recieved
    send(message_recieved, broadcast=True)
    message_counter+=1


## TODO
## Player hits play and that generates: 
##   - Game ID
##   - Route with Game ID
##   - Database entry with Game ID
@socketio.on("play")
def play_game():
    send("Game starting.. Setting up players", broadcast=True)
    send(f"Players in action are: {player_names}", broadcast=True)

    import itertools as it
    player = it.cycle([*munchkin.players.values()]) # cool built in module that allows for cycling through each player turn
    # while munchkin.check_game_over(): # this checks if any body has won before calling on next player
    current_player = next(player) # next() is part of the iter module to call on next items in an iterable
    send(json.dumps(munchkin.play(current_player)), broadcast=True)
    send("ping is not awesome!", broadcast=True)
    return json.dumps(munchkin.play(current_player)) #send(f"Game Over: {current_player.name} has won the game!", broadcast=True)

if __name__ == '__main__':
    socketio.run(app)