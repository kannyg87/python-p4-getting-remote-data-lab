import requests
import json

class GetRequester:
    url = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        programs_list = []
        programs = json.loads(self.get_response_body())
        for program in programs:
            programs_list.append(program)

        return programs_list