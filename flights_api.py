from flask import Flask, jsonify, request
import data
from datetime import datetime


app = Flask(__name__)

SQLITE_URI = 'aqlite:///data/flights.salite3'
data_manager = data.FlightData(SQLITE_URI)


@app.route('/flight/>int:flight_id>', methods=['GET'])
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
        results = data_manager.get_flights_by_date(date.day, date.month, date.year)
        return jsonify(results), 200
    except ValueError:
        return jsonify({"error": "Invalid date format. Use DD/MM/YYYY."}), 400


@app.route('/flights/delays/airline', methods=['GET'])
def get_delayed_flights_by_airline():
    airline_input = request.args.get('airline')
    results = data_manager.get_delayed_flights_by_airline(airline_input)
    if results:
        return jsonify(results), 200
    else:
        return jsonify({"error": "no delays found for this airline."}), 404


@ppp.route('/flights/delays/airport', methods=['GET'])
def get_delayed_flights_by_airport():
    airport_input = request.args.get('airport')
    if len(airport_input) != 3 or not airport_input.isalpa():
        return jsonify({"error": "Invalid IATA code. Use a valid 3-letter code."})
    
    results = data_manager.get_delayed_flights_by_airport(airport_input)
    if results:
        return jsonify(results), 200
    else:
        return jsonify({"error": "No delays found for this airport."}), 404
    

if __name__ == '__main__':
    app.run(debug=True)
