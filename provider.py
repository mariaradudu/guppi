from repository import Repository
from generator import Generator


class WeatherProvider:

    def __init__(self):

        self.repo = Repository()

        self.generator = Generator()

    def forecast(self, city):

        data = self.repo.get(city.name)

        if not data:

            return None

        return self.generator.create(
            city.name,
            data
        )
