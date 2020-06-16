from flask import Flask, render_template, request

import numpy as np
from model import predict

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roll_dice/<num_of_dice>')
def roll_dice(num_of_dice):
    random_numbers = np.random.randint(1, 6, int(num_of_dice))
    return render_template('roll_dice.html', rolls=random_numbers)

@app.route('/check_text_form')
def check_text_form():
    return render_template('check_text_form.html')

@app.route('/check_text_results', methods=['POST'])
def handle_check_text_form(): 
    text_content = request.form['text-content']

    text_results = predict(text_content)

    return render_template('check_text_results.html', text_results=text_results)