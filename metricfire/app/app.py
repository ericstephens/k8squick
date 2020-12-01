#https://www.metricfire.com/blog/develop-and-deploy-a-python-api-with-kubernetes-and-docker-part-ii/

from flask import Flask
import requests
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'App Works!!!!'

@app.route('/reverse/<string:str>')
def reverse(str):
    data = str + ":" + str[::-1]
    return data

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)