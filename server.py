from flask import Flask, render_template
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roll_dice/<num_of_dice>')
def roll_dice(num_of_dice):
    random_numbers = np.random.randint(1, 6, int(num_of_dice))
    return render_template('roll_dice.html', rolls=random_numbers)