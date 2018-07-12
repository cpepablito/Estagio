from flask import Flask, render_template
from flask_socketio import SocketIO, emit

socketio = SocketIO(app)
app.config['SECRET_KEY'] = 'secret!'

thread = Thread()
thread_stop_event = Event()
class RandomThread(Thread):
    def __init__(self):
        self.delay = 1
        super(RandomThread, self).__init__()
    def randomNumberGenerator(self):
        """
        Generate a random number every 1 second and emit to a socketio instance (broadcast)
        Ideally to be run in a separate thread?
        """
        #infinite loop of magical random numbers
        print("Making random numbers")
        while not thread_stop_event.isSet():
            state = random.randint(0, 1)
            socketio.emit('newstate', {'state': state}, namespace='/test')
            sleep(self.delay)
    def run(self):
        self.randomNumberGenerator()
