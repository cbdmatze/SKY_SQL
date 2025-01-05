---

# SKY_SQL

**SKY_SQL** is a Python-based flight data management program that uses an SQLite database to store and query detailed flight information. This program provides an interactive command-line interface (CLI) that allows users to query flights, view flight delays, and visualize the results using graphs. The flight data includes details such as airlines, airports, flight IDs, delays, and scheduled flight times.

With a focus on simplicity and efficiency, **SKY_SQL** allows users to:
- Retrieve flight details by ID.
- Query flights by specific dates.
- Find delayed flights by airline or airport.
- Visualize flight delay data with easy-to-understand plots.

## Features

- **Flight Search by ID**: Fetch flight details for a specific flight using its unique ID.
- **Flights by Date**: Query flights scheduled for a specific date in DD/MM/YYYY format.
- **Delayed Flights by Airline**: Retrieve and visualize delayed flights for a specific airline.
- **Delayed Flights by Airport**: Retrieve and visualize delayed flights for a specific airport using the IATA airport code.
- **Graphical Visualization**: Plot graphs for delayed flights by airline, airport, and specific dates using `matplotlib`.

## Requirements

The program relies on several libraries and modules. To run **SKY_SQL**, make sure you have the following installed:

### Python Libraries:
- `matplotlib`: For generating plots and visualizations.
- `sqlalchemy`: For handling the SQLite database and executing SQL queries.
- `datetime`: For parsing and formatting dates.
  
These libraries can be installed via pip with the following command:

```bash
pip install matplotlib sqlalchemy
```

## Database Setup

**SKY_SQL** requires an SQLite database containing flight information. The database should have the following structure:

| Column             | Data Type | Description                              |
|--------------------|-----------|------------------------------------------|
| ID                 | Integer   | Unique identifier for the flight         |
| AIRLINE            | String    | Name of the airline operating the flight |
| ORIGIN_AIRPORT     | String    | IATA code of the origin airport          |
| DESTINATION_AIRPORT| String    | IATA code of the destination airport     |
| DELAY              | Integer   | Delay time in minutes (if any)           |
| FLIGHT_DATE        | Date      | Date when the flight is scheduled        |

An example SQLite database named `flights.sqlite3` is expected to reside in the `data` directory within the project.

## Program Structure

The **SKY_SQL** program is structured into multiple modules for ease of maintenance and scalability:

1. **main.py**: The entry point of the program, which handles user interaction and provides a command-line menu.
2. **data.py**: This module contains the `FlightData` class, which handles communication with the SQLite database using SQLAlchemy.
3. **plot.py**: This module contains functions for plotting graphs to visualize flight delays by airlines, airports, and dates.

### Menu Options

When the program is executed, the user is presented with the following options:

- **1. Show flight by ID**: Query flight details by entering a specific flight ID.
- **2. Show flights by date**: Query and view flights scheduled for a specific date.
- **3. Show delayed flights by airline**: View delayed flights for a given airline and visualize the results.
- **4. Show delayed flights by airport**: View delayed flights for a given origin airport (IATA code) and visualize the results.

### Example Usage

Here’s an example of how the program works:

1. Run the program:
   ```bash
   python main.py
   ```

2. You will be presented with a menu like this:
   ```
   Welcome to Flight Data Manager
   Menu:
   1. Show flight by ID
   2. Show flights by date
   3. Show delayed flights by airline
   4. Show delayed flights by airport
   ```

3. Select an option by entering the corresponding number:
   - **Option 1 (Show flight by ID)**: Input a flight ID (e.g., `123`), and the program will display the flight details for that ID.
   - **Option 2 (Show flights by date)**: Input a date in DD/MM/YYYY format (e.g., `25/12/2024`), and the program will show all flights scheduled on that date.
   - **Option 3 (Show delayed flights by airline)**: Input an airline name (e.g., `Delta`), and the program will show all delayed flights for that airline.
   - **Option 4 (Show delayed flights by airport)**: Input an origin airport IATA code (e.g., `JFK`), and the program will show all delayed flights originating from that airport.

4. Visualizations:
   - If any flight delays are found, the program will generate and display a graph using `matplotlib` to help visualize the delay data.

## Code Overview

Here is a brief overview of the key modules in **SKY_SQL**:

### 1. main.py

This file contains the core logic for the command-line interface, user input, and menu navigation. The program begins by displaying a menu and allows the user to select from various options to retrieve flight data.

### 2. data.py

The `data.py` module contains the `FlightData` class, which handles interaction with the SQLite database using SQLAlchemy. This class provides methods such as:
- `get_flight_by_id(id)`
- `get_flights_by_date(day, month, year)`
- `get_delayed_flights_by_airline(airline)`
- `get_delayed_flights_by_airport(airport)`

### 3. plot.py

This module contains plotting functions to visualize the flight delay data. It uses `matplotlib` to generate the following types of plots:
- **Delays by Airline**
- **Delays by Airport**
- **Flights on a Specific Date**

## File Structure

```
SKY_SQL/
├── data/
│   ├── flights.sqlite3        # SQLite database with flight data
├── main.py                    # Entry point of the application
├── data.py                    # Database interaction module
├── plot.py                    # Module for plotting graphs
└── README.md                  # Program documentation (this file)
```

## Future Enhancements

- **More Query Options**: The program could be extended to allow querying by other attributes such as destination airport, flight duration, etc.
- **Advanced Visualizations**: Future versions may include more advanced data visualization options like heat maps for flight delays across different airports and airlines.
- **Web Interface**: The program could be further enhanced by adding a web-based interface for easier interaction, or even a REST API for external integrations.

## Conclusion

**SKY_SQL** is a simple yet powerful tool for managing and querying flight data. With its intuitive interface and ability to visualize delays, it provides great insight into flight patterns and delays. Whether you're an airline analyst or just interested in exploring flight data, **SKY_SQL** makes the process easy and informative.

Feel free to contribute or suggest new features to enhance this program even further!

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---
