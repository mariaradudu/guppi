from forecast import Forecast


class Generator:

    def create(
        self,
        city,
        data
    ):

        return Forecast(

            city,

            data["condition"],

            data["temperature"],

            data["humidity"],

            data["wind"]

        )
