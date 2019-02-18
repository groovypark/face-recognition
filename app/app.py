import os

import requests
from flask import Flask, flash, request, jsonify, abort

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__, static_folder='../spa/build', static_url_path='')

CLIENT_ID = {'X-Naver-Client-Id': 'Xsu4cZdem_jHXs4Jhcgu'}
CLIENT_SECRET = {'X-Naver-Client-Secret': os.environ["CLIENT_SECRET"]}
CFR_API_URL = 'https://openapi.naver.com/v1/vision/celebrity'
CONTENT_TYPE = {'Content-Type': 'multipart/form-data'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return abort(400)
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        flash('No selected file')
        return abort(400)
    if file and allowed_file(file.filename):

        response = requests.post(url=CFR_API_URL, headers={**CLIENT_ID, **CLIENT_SECRET}, files=dict(image=file))

        if response.status_code != 200:
            message = response.json()["errorMessage"]
            return jsonify({"message": message}), response.status_code
        return jsonify(response.json()), response.status_code
    return abort(400)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
