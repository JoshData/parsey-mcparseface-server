#!/usr/bin/python3

# sudo apt-get install python3-pip
# sudo pip3 install flask

import os
from flask import Flask, request, Response
from multiprocessing import Pool
from parser import parse_sentence
import json

app = Flask(__name__)
port = 80 if os.getuid() == 0 else 8000

pool = Pool(5, maxtasksperchild=10)

@app.route('/')
def index():
  q = request.args.get("q", "")
  result = pool.apply(parse_sentence, [q])

  return Response(
    response=json.dumps(result, indent=2),
    status=200,
    content_type="application/json")

if __name__ == '__main__':
    app.run(debug=True, port=port, host="0.0.0.0")

