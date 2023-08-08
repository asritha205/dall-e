from flask import Flask,jsonify
from flask import render_template
import os
import openai
from config import key
openai.api_key=key
app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',)
@app.route('/generateimage/<prompt>')
def generate(prompt):
    print("p:",prompt)
    response = openai.Image.create(prompt=prompt,
                                   n=1,
                                   size="256x256")
    print(response)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug = True, port = 8000)
