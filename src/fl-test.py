"""doc string goes here"""

from flask import Flask, url_for, jsonify, request
app = Flask(__name__)

from utils.checker import exclame

@app.route('/')
def hello_world():
  return exclame('hi')
  # obj = { 'name': 'Rob', 'pic':'sample.jpg' }
  # return jsonify(obj)

app.run()