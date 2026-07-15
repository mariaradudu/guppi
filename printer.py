def show(forecast):

    if forecast is None:

        print("Forecast unavailable.")

        return

    print()

    print("Weather Mock")

    print("-" * 30)

    print(f"Location : {forecast.city}")

    print()

    print(f"Condition : {forecast.condition}")

    print(f"Temperature : {forecast.temperature}°C")

    print(f"Humidity : {forecast.humidity}%")

    print(f"Wind : {forecast.wind} km/h")

    print()

    print("-" * 30)

    print("Forecast generated successfully.")
