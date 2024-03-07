from flask import Flask, request, jsonify
import cv2 as cv
import numpy as np

from model.model_detector import ModelDetector

app = Flask(__name__)
model = ModelDetector()

@app.route('/')
def index():
    return "yello"


frame = None  # global variable to keep single JPG


@app.route('/upload/<string:lookup_sign>', methods=['PUT'])
def upload(lookup_sign):
    global frame
    # keep jpg data in global variable
    frame = request.data
    decoded = cv.imdecode(np.frombuffer(request.data, np.uint8), -1)
    print("RECEIVED REQUEST WITH SIGN: ", lookup_sign)
    return jsonify(model.detect(decoded, lookup_sign))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
