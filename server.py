from flask import Flask
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/roll_dice/<num_of_dice>')
def roll_dice(num_of_dice):
    random_number = np.random.randint(1, 6, int(num_of_dice))
    return str(random_number)