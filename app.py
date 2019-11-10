from flask import Flask
from flask import jsonify
import math_api

app = Flask(__name__)

@app.route('/')
def hello():
    d = math_api.choose_phase()
    message = {
        'status': 200,
        'message': 'OK',
        'scores': d
    }
    resp = jsonify(message)
    resp.status_code = 200
    print(resp)
    return resp

if __name__ == '__main__':
    app.run()