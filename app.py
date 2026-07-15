from city import City
from provider import WeatherProvider
from printer import show

provider = WeatherProvider()

rome = City("Rome")

forecast = provider.forecast(rome)

show(forecast)
