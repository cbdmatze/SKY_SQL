import data
import plot
from datetime import datetime

SQLITE_URI = 'sqlite:///data/flights.sqlite3'
IATA_LENGTH = 3


def delayed_flights_by_airline(data_manager):
    """
    Prompts the user to input an airline name, retrieves delayed flights for that airline using
    the data manager, and prints the results. If results are found, a plot of flight delays is generated.

    Args:
        data_manager(FlightData): Instance of the FlightData class to interact with the database.
    """
    airline_input = input("Enter airline name: ")
    results = data_manager.get_delayed_flights_by_airline(airline_input)
    print_results(results)
    if results:
        plot.plot_flight_delays_by_airline(results)
    else:
        print("No delays found for this airline.")


def delayed_flights_by_airport(data_manager):
    """
    Prompts the user to input a valid IATA 3-letter airport code, retrieves delayed flights for that
    airport using the data manager, and prints the results. If results are found, a plot of flight delays is generated.
    
    Args:
        data_manager (FlightData): Instance of the FlightData class to interact with the database.
    """
    valid = False
    while not valid:
        airport_input = input("Enter origin airport IATA code: ")
        if airport_input.isalpha() and len(airport_input) == IATA_LENGTH:
            valid = True
    results = data_manager.get_delayed_flights_by_airport(airport_input)
    print_results(results)
    if results:
        plot.plot_flight_delays_by_airport(results)
    else:
        print("No delays found for this airport.")


def flight_by_id(data_manager):
    """
    Prompts the user to input a flight ID, retrieves the flight details for that ID using 
    the data manager, and prints the results.
    
    Args:
        data_manager (FlightData): Instance of the FlightData class to interact with the database.
    """
    valid = False
    while not valid:
        try:
            id_input = int(input("Enter flight ID: "))
        except ValueError:
            print("Invalid input. Please enter a valid numeric flight ID.")
        else:
            valid = True
    results = data_manager.get_flight_by_id(id_input)
    print_results(results)


def flights_by_date(data_manager):
    """
    Prompts the user to input a date in DD/MM/YYYY format, retrieves flights on that date 
    using the data manager, and prints the results. If results are found, a plot of the flights is generated.
    
    Args:
        data_manager (FlightData): Instance of the FlightData class to interact with the database.
    """
    valid = False
    while not valid:
        try:
            date_input = input("Enter date in DD/MM/YYYY format: ")
            date = datetime.strptime(date_input, '%d/%m/%Y')
        except ValueError as e:
            print(f"Invalid date format. Try again: {e}")
        else:
            valid = True
    
    results = data_manager.get_flights_by_date(date.day, date.month, date.year)
    print_results(results)
    if results:
        plot.plot_flights_by_date(results)
    else:
        print("No flights found for this date.")


def print_results(results):
    """
    Takes the list of flight results and prints each flight's information. If a flight
    has a delay, it will also show the delay time.
    
    Args:
        results (list): List of flight result dictionaries from the database query.
    """
    print(f"Got {len(results)} results.")
    for result in results:
        result = result._mapping
        try:
            delay = int(result['DELAY']) if result['DELAY'] else 0
            origin = result['ORIGIN_AIRPORT']
            dest = result['DESTINATION_AIRPORT']
            airline = result['AIRLINE']
        except KeyError as e:
            print(f"Error showing results: {e}")
            return
        
        if delay > 0:
            print(f"{result['ID']}. {origin} -> {dest} by {airline}, Delay: {delay} Minutes")
        else:
            print(f"{result['ID']}. {origin} -> {dest} by {airline}")


def show_menu_and_get_input():
    """
    Displays a menu of options and prompts the user to select one.
    The user can select from several functions related to flight data.
    
    Returns:
        function: The function corresponding to the selected menu option.
    """
    print("Menu:")
    for key, value in FUNCTIONS.items():
        print(f"{key}. {value[1]}")

    while True:
        try:
            choice = int(input())
            if choice in FUNCTIONS:
                return FUNCTIONS[choice][0]
        except ValueError:
            pass
        print("Invalid selection. Please try again.")


FUNCTIONS = {
    1: (flight_by_id, "Show flight by ID"), 
    2: (flights_by_date, "Show flights by date"), 
    3: (delayed_flights_by_airline, "Show delayed flights by airline"), 
    4: (delayed_flights_by_airport, "Show delayed flights by airport"),
}


def main():
    """
    Main entry point of the program. Initializes the data manager and enters the main menu loop,
    allowing the user to interact with the flight data.
    """
    print("Welcome to Flight Data Manager:")
    data_manager = data.FlightData(SQLITE_URI)

    while True:
        selected_func = show_menu_and_get_input()
        selected_func(data_manager)


if __name__ == "__main__":
    main()
