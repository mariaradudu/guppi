from sample_weather import DATA


class Repository:

    def get(self, city):

        return DATA.get(city)
