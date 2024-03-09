from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2 as cv
import numpy as np

from car_data import CarData
from model.model_detector import ModelDetector

app = Flask(__name__)
CORS(app)

model = ModelDetector()
car_data = CarData()

frame = None  # global variable to keep single JPG


@app.route('/')
def index():
    return "yello"


@app.route('/upload/<string:lookup_sign>', methods=['PUT'])
def upload(lookup_sign):
    global frame
    # keep jpg data in global variable
    frame = request.data
    decoded = cv.imdecode(np.frombuffer(request.data, np.uint8), -1)
    print("RECEIVED REQUEST WITH SIGN: ", lookup_sign)
    return jsonify(model.detect(decoded, lookup_sign))


@app.route('/steer', methods=['POST'])
def steer():
    if request.method == 'POST':
        data = request.json
        car_data.set_steering(data['steer'])
        return jsonify({'message': 'Steering status updated successfully'}), 200
    else:
        return jsonify({'error': 'Only POST requests are accepted'}), 405


@app.route('/speed', methods=['POST'])
def speed():
    if request.method == 'POST':
        data = request.json
        car_data.set_speed(data['speed'])
        return jsonify({'message': 'Speed status updated successfully'}), 200
    else:
        return jsonify({'error': 'Only POST requests are accepted'}), 405


@app.route('/sign', methods=['POST'])
def sign():
    if request.method == 'POST':
        data = request.json
        car_data.set_sign(data['sign'])
        return jsonify({'message': 'Sign status updated successfully'}), 200
    else:
        return jsonify({'error': 'Only POST requests are accepted'}), 405


@app.route('/brake', methods=['POST'])
def brake():
    if request.method == 'POST':
        data = request.json
        car_data.set_braking(data['braking'])
        return jsonify({'message': 'Braking status updated successfully'}), 200
    else:
        return jsonify({'error': 'Only POST requests are accepted'}), 405


@app.route('/car-data', methods=['GET'])
def get_car_data():
    return jsonify({
        'steer': car_data.get_steering(),
        'speed': car_data.get_speed(),
        'sign': car_data.get_sign(),
        'brake': car_data.get_braking()
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
