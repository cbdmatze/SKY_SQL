import matplotlib.pyplot as plt

def plot_flight_delays_by_airline(results):
    """
    Plots the number of delayed flights per airline.
    """
    airlines = [r['airline'] for r in results]
    delays = [r['DELAY'] for r in results]

    plt.bar(airlines, delays)
    plt.xlabel('Airline')
    plt.ylabel('Delay (minutes)')
    plt.title('Flight Delays by Airline')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_flight_delays_by_airport(results):
    """
    Plots the delay distribution for a specific airport.
    """
    destinations = [r['DESTINATION_AIRPORT'] for r in results]
    delays = [r['DELAY'] for r in results]

    plt.bar(destinations, delays)
    plt.xlabel('Destination Airport')
    plt.ylabel('Delay (minutes)')
    plt.title('Flight Delay by Destination Airport')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_flights_by_date(results):
    """
    Plots the flight delays for a specific date.
    """
    flights = [f"{r['ORIGIN_AIRPORT']}->{r['DESTINATION_AIRPORT']}" for r in results]
    delays = [r['DELAY'] for r in results]

    plt.bar(flights, delays)
    plt.xlabel('Flight Route')
    plt.ylabel('Delay (minutes)')
    plt.title('Flight Delays on Date')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()
