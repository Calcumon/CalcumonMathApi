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
        'message': 'OK',
        'phase1': [
            {
            'eqn1': phase1[0][0],
            'ans1': phase1[0][1],
            'guesses1': phase1_guesses[0],
            },
            {
            'eqn2': phase1[1][0],
            'ans2': phase1[1][1],
            'guesses2': phase1_guesses[1]
            },
            {
            'eqn3': phase1[2][0],
            'ans3': phase1[2][1],
            'guesses3': phase1_guesses[2]
            },
            {
            'eqn4': phase1[3][0],
            'ans4': phase1[3][1],
            'guesses4': phase1_guesses[3]
            },
            {
            'eqn5': phase1[4][0],
            'ans5': phase1[4][1],
            'guesses5': phase1_guesses[4]
            },
            {
            'eqn6': phase1[5][0],
            'ans6': phase1[5][1],
            'guesses6': phase1_guesses[5]
            },
            {
            'eqn7': phase1[6][0],
            'ans7': phase1[6][1],
            'guesses7': phase1_guesses[6]
            },
            {
            'eqn8': phase1[7][0],
            'ans8': phase1[7][1],
            'guesses8': phase1_guesses[7]
            },
            ]
        # 'phase2': [{
        #     'eqn': p2eqn2,
        #     'ans': p2ans2,
        #     'guesses': p2guesses2
        # }]
        # 'phase3': [{
        #     'eqn': p3eqn3,
        #     'ans': p3ans3,
        #     'guesses': p3guesses3
        # }]
    }
    resp = jsonify(message)
    resp.status_code = 200
    print(resp)
    return resp

if __name__ == '__main__':
    app.run()