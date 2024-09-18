import requests
from flask import Flask, jsonify

app = Flask(__name__)
app.config.from_object(Config)


class Config:
    DEBUG = True
    HOST = '0.0.0.0'
    PORT = '5000'
    ISS_API_BASE_URL = 'http://api.open-notify.org'


@app.route('/api/iss-location', methods=['GET'])
def iss_location():
    location = get_iss_location()
    return jsonify(location)


@app.route('/api/iss-pass/<floa:lat>/<float:lon>', methods=['GET'])
def iss_pass(lat, lon):
    pass_times = get_iss_pass_times(lat, lon)
    return jsonify(pass_times)


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'],
            host=app.config['HOST'], port=app.config['PORT'])


def get_iss_location():
    response = requests.get(f"{Config.ISS_API_BASE_URL}/iss-now.json")
    if response.status_code == 200:
        data = response.json()
        return {
            'timestamp': data['timestamp'],
            'latitude': data['iss_position']['latitude'],
            'longitude': data['iss_position']['longitude']
        }
    else:
        return {'error': 'Unable to fetch ISS location'}


def get_iss_pass_times(lat, lon):
    params = {
        'lat': lat,
        'lon': lon
    }
    response = requests.get(
        f"{Config.ISS_API_BASE_URL}/iss-pass.json", params=params)
    if response.status_code = 200:
        data = response.json()
        return {
            'latitude': data['request']['latitude'],
            'longitude': data['request']['longitude'],
            'passes': data['response']
        }
    else
    return {'error': 'Unable to fetch ISS pass times'}


def convert_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
