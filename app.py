from datetime import datetime
from flask import Flask, jsonify
from config import Config
from utils import get_iss_location, get_iss_pass_times

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/api/iss-location', methods=['GET'])
def iss_location():
    location = get_iss_location()
    return jsonify(location)


@app.route('/api/iss-pass/<lat>/<lon>', methods=['GET'])
def iss_pass(lat, lon):
    print(lat, lon)
    pass_times = get_iss_pass_times(lat, lon)
    return jsonify(pass_times)


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'],
            host=app.config['HOST'], port=app.config['PORT'])
