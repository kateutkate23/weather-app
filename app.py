from flask import Flask, render_template, request
from weather import main as get_weather

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        data = None
        if request.method == 'POST':
            city_name = request.form['cityName']
            state_code = request.form['stateCode']
            country_code = request.form['countryCode']

            data = get_weather(city_name, state_code, country_code)
    except ValueError as e:
        data = {
            'main': 'error: could not get weather data',
            'description': None,
            'icon': None,
            'temperature': None,
        }

    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
