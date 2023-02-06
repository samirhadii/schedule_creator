from flask import Flask, jsonify


from schedule import set_schedule
from coordinates import get_coords

app = Flask(__name__)


@app.route('/make_schedule/<street>/<city>/<state>/<zipcode>/<radius>/<int:desired_price>')
def get_schedule(street, city, state, zipcode, radius, desired_price):

    coordinates = get_coords(street, city, state, zipcode)
    schedule = set_schedule(coordinates, desired_price, radius)
    json_schedule = jsonify(schedule)

    return json_schedule


if __name__ == '__main__':
    app.run(debug=True)
