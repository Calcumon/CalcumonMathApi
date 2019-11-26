import math_api
import random

from flask import Flask
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    phase1 = math_api.choose_phase(1)
    phase1_guesses = []
    for item in phase1:
        phase1_guesses.append(math_api.gen_guesses(0, 10, 5, item[1]))
    message = {
        'status': 200,
        'eqn_ans': phase1,
        'guesses': phase1_guesses
    }
    resp = jsonify(message)
    resp.status_code = 200
    print(resp)
    return resp

if __name__ == '__main__':
    app.run()