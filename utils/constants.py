from enum import Enum

API_URL = "https://web-series-quotes-api.deta.dev"
TOKEN = "5901095507:AAGY82HNbO2DDIht5GRSnQmbIsDvBBDdpss"


class SeriesEnum(str, Enum):
    breaking_bad = "breaking_bad"
    dark = "dark"
    game_of_thrones = "game_of_thrones"
    money_heist = "money_heist"
