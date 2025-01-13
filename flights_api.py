from flask import Flask, jsonify, request
import data
from datetime import datetime


app = Flask(__name__)

SQLITE_URI = 'sqlite:///data/flights.sqlite3'  # Fixed URI
data_manager = data.FlightData(SQLITE_URI)


@app.route('/flight/<int:flight_id>', methods=['GET'])  # Fixed route
def get_flight_by_id(flight_id):
    results = data_manager.get_flight_by_id(flight_id)
    if results:
        return jsonify(results), 200
    else:
        return jsonify({"error": "Flight not found"}), 404


@app.route('/flights/date', methods=['GET'])
def get_flights_by_date():
    date_input = request.args.get('date')
    try:
        date = datetime.strptime(date_input, '%d/%m/%Y')
    except ValueError:
        return jsonify({"error": "Invalid date format. Use DD/MM/YYYY."}), 400
    results = data_manager.get_flights_by_date(date.day, date.month, date.year)
    if results:
        return jsonify(results), 200
    else:
        return jsonify({"error": "No flights found."}), 404


@app.route('/flights/delays/airport', methods=['GET'])  # Fixed typo
def get_delayed_flights_by_airport():
    airport = request.args.get('airport')
    results = data_manager.get_delayed_flights_by_airport(airport)
    if results:
        return jsonify(results), 200
    else:
        return jsonify({"error": "No delayed flights for this airport."}), 404


@app.route('/flights/delays/airline', methods=['GET'])
def get_delayed_flights_by_airline():
    airline = request.args.get('airline')
    results = data_manager.get_delayed_flights_by_airline(airline)
    if results:
        return jsonify(results), 200
    else:
        return jsonify({"error": "No delayed flights for this airline."}), 404


if __name__ == '__main__':
    app.run(debug=True)
