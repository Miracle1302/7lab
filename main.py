# Dictionary to store weather data
weather_data = {
    "01-01": (-3, 5),  # Format: (temperature, precipitation)
    "02-01": (2, 10),
    "03-01": (5, 12),
    "04-01": (-1, 7),
    "05-01": (0, 0)
}

def print_weather_data():

    for date, (temp, precip) in weather_data.items():
        print(f"Date: {date}, Temperature: {temp}°C, Precipitation: {precip} mm")

def add_or_update_entry(date, temperature, precipitation):

    weather_data[date] = (temperature, precipitation)
    print(f"Data for {date} updated.")

def delete_entry(date):

    try:
        del weather_data[date]
        print(f"Data for {date} deleted.")
    except KeyError:
        print(f"No data for {date} exists in the dictionary.")

def view_sorted_weather_data():

    sorted_dates = sorted(weather_data.keys())
    for date in sorted_dates:
        temp, precip = weather_data[date]
        print(f"Date: {date}, Temperature: {temp}°C, Precipitation: {precip} mm")

def calculate_precipitation_type():

    rain = 0
    snow = 0
    for temp, precip in weather_data.values():
        if temp > 0:
            rain += precip
        else:
            snow += precip
    print(f"Amount of precipitation as rain: {rain} mm, as snow: {snow} mm")

def main():
    while True:
        print("\n1. Display all weather data")
        print("2. Add/Update weather data")
        print("3. Delete weather data")
        print("4. Show sorted data")
        print("5. Calculate type of precipitation")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            print_weather_data()
        elif choice == '2':
            date = input("Enter the date (dd-mm): ")
            temp = int(input("Enter the temperature: "))
            precip = int(input("Enter the amount of precipitation: "))
            add_or_update_entry(date, temp, precip)
        elif choice == '3':
            date = input("Enter the date to delete (dd-mm): ")
            delete_entry(date)
        elif choice == '4':
            view_sorted_weather_data()
        elif choice == '5':
            calculate_precipitation_type()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()

