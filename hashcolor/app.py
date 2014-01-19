from flask import Flask, render_template, jsonify, request
from hashcolor.hashing import string_to_color

app = Flask(__name__)

@app.route('/')
def index():
    hashcolor = string_to_color(request.remote_addr)
    return render_template('index.html', hash_color=hashcolor)

@app.route('/<name>/')
def hashit(name):
    hashcolor = string_to_color(name)
    return jsonify(hashcolor=hashcolor)

if __name__ == "__main__":
    app.run()
