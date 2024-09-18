import requests
from config import Config
from datetime import datetime


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
    try:
        response = requests.get(
            f"{Config.ISS_API_BASE_URL}/iss-pass.json", params=params)
        if response.status_code == 200:
            data = response.json()
            return {
                'latitude': data['request']['latitude'],
                'longitude': data['request']['longitude'],
                'passes': data['response']
            }
        else:
            return {'error': f'Unable to fetch ISS pass times {response.status_code}'}
    except Exception as e:
        print(e)
        return {'error': str(e)}


def convert_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
