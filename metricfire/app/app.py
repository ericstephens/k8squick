from flask import Flask
import requests

app = Flask(__name__)

API_KEY = "47528ff57f24344dd3b93b4564e9df1e"

@app.route('/')
def index():
    return 'App Works!!!!'

@app.route('/reverse/<string:str>')
def reverse(str):
    data = str[::-1]
    return data

@app.route('/<string:city>')
def weather_by_city(city):

# https://samples.openweathermap.org/data/2.5/weather?

    #test =  "https://api.openweathermap.org/data/2.5/weather?q=London&appid=b43cb98f3b3d2006fcfb8524bb058ba9"

    url = 'https://samples.openweathermap.org/data/2.5/weather'
    params = dict(
        q=city,
        appid=API_KEY,
    )

    print(params)

    response = requests.get(url=url, params=params)
    data = response.json()
    return data

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)