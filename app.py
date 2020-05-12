import os
import sys
import time
import datetime
import io
import logging
import traceback
from flask import Flask, send_from_directory, jsonify, request
from flask_cors import CORS, cross_origin


# Bind to PORT if defined, otherwise default to 5000.
port = int(os.environ.get('PORT', 5000))
app = Flask(__name__)

CORS(app)

@app.route('/')
def root_html():
    return 'ack'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, threaded=True)