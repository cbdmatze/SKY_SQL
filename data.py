from sqlalchemy import create_engine, text

# SQL Queries
QUERY_FLIGHT_BY_ID = """
    SELECT
        flights.*, 
        airlines.name as airline, 
        flights.ID as FLIGHT_ID, 
        flights.DEPARTURE_DELAY as DELAY
    FROM
        flights
    JOIN
        airlines
        ON flights.airline = airlines.id
    WHERE
        flights.ID = :id
"""

QUERY_DELAYED_FLIGHTS_BY_AIRLINE = """
    SELECT
        flights.ORIGIN_AIRPORT, flights.DESTINATION_AIRPORT,
        flights.DEPARTURE_DELAY as DELAY, airlines.name as airline
    FROM
        flights
    JOIN 
        airlines
        ON flights.airline = airlines.id
    WHERE
        airlines.name LIKE :airline AND flights.DEPARTURE_DELAY > 0
"""

QUERY_DELAYED_FLIGHTS_BY_AIRPORT = """
    SELECT
        flights.ORIGIN_AIRPORT, flights.DESTINATION_AIRPORT,
        flights.DEPARTURE_DELAY as DELAY, airlines.name as airline
    FROM
        flights
    JOIN
        airlines
        ON flights.airline = airlines.id
    WHERE
        flights.ORIGIN_AIRPORT = :airport AND flights.DEPARTURE_DELAY > 0
"""

QUERY_FLIGHTS_BY_DATE = """
    SELECT
        flights.ORIGIN_AIRPORT, flights.DESTINATION_AIRPORT,
        flights.DEPARTURE_DELAY as DELAY, airlines.name as airline, flights.FLIGHT_DATE
    FROM
        flights
    JOIN
        airlines
        ON flights.airline = airlines.id
    WHERE 
        DATE(flights.FLIGHT_DATE) = :flight_date
"""

class FlightData:
    def __init__(self, db_uri):
        """Initialize a new engine using the given database URI."""
        self._engine = create_engine(db_uri)
    
    def _execute_query(self, query, params):
        """Executes a SQL query with params and returns a list of records."""
        try:
            with self._engine.connect() as connection:
                result = connection.execute(text(query), params)
                return result.mappings().all()
        except Exception as e:
            print(f"Error executing query: {e}")
            return []
    
    def get_flight_by_id(self, flight_id):
        """Returns flight details for a specific flight ID."""
        params = {'id': flight_id}
        return self._execute_query(QUERY_FLIGHT_BY_ID, params)
    
    def get_delayed_flights_by_airline(self, airline_name):
        """Returns delayed flight details for a specific airline."""
        params = {'airline': f"%{airline_name}%"} # Partial match for flexibility
        return self._execute_query(QUERY_DELAYED_FLIGHTS_BY_AIRLINE, params)
    
    def get_delayed_flights_by_airport(self, airport_code):
        """Returns delayed flight details for a specific airport."""
        params = {'airport': airport_code.upper()} # Ensure airport code is in uppercase
        return self._execute_query(QUERY_DELAYED_FLIGHTS_BY_AIRPORT, params)
   
    def get_flights_by_date(self, day, month, year):
        """Returns flights for a specific date."""
        formatted_date = f"{year}-{month:02d}-{day:02d}"  # Fixed date format
        params = {'flight_date': formatted_date}
        return self._execute_query(QUERY_FLIGHTS_BY_DATE, params)
    
    def __del__(self):
        """Closes the database connection."""
        self._engine.dispose()
