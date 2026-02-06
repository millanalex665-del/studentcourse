import json

class DataStore:
    FILE = "data.json"

    @staticmethod
    def load_data():
        try:
            with open(DataStore.FILE, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {"students": {}, "courses": {}}

    @staticmethod
    def save_data(data):
        with open(DataStore.FILE, "w") as file:
            json.dump(data, file, indent=4)
