# Weather Mock

Weather Mock is a fake weather service designed for development and testing.

Instead of requesting data from an online weather API, the application returns predefined forecasts that can be used while building other software.

---

## Example

```
Weather Mock

Location : Rome

Condition : Sunny

Temperature : 28°C

Humidity : 43%

Wind : 12 km/h

------------------------

Forecast generated successfully.
```

---

## Files

| File | Purpose |
|------|---------|
| app.py | Starts the application |
| provider.py | Supplies weather data |
| repository.py | Stores mock forecasts |
| forecast.py | Forecast model |
| generator.py | Builds forecast objects |
| printer.py | Displays weather |
| sample_weather.py | Example dataset |
| city.py | City model |

---

## Launch

```
python app.py
```

Mock data only. No Internet connection required.
