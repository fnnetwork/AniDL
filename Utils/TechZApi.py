import requests


class Gogo:
    def __init__(self) -> None:
        self.base = "https://api3.shubhamkr-sk8016.workers.dev"

    def gogo_search(self, query):
        data = requests.get(f"{self.base}/search/{query}").json()
        return data["results"]

    def gogo_anime(self, id):
        data = requests.get(f"{self.base}/anime/{id}").json()
        return data

    def gogo_episode(self, id):
        data = requests.get(f"{self.base}/episode/{id}").json()
        return data


class TechZApi(Gogo):
    def __init__(self) -> None:
        self.base = "https://api3.shubhamkr-sk8016.workers.dev"
        super().__init__()
