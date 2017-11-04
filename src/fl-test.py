"""doc string goes here"""

from flask import Flask, url_for, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
  obj = { 'name': 'Rob', 'pic':'sample.jpg' }
  return jsonify(obj)

