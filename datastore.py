import json
import os

class DataStore:
    FILE_NAME = "data.json"

    @staticmethod
    def load_data():
        if os.path.exists(DataStore.FILE_NAME):
            try:
                with open(DataStore.FILE_NAME, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                # If file is corrupted, return default structure
                return {"students": {}, "courses": {}}
        
        return {"students": {}, "courses": {}}

    @staticmethod
    def save_data(data):
        with open(DataStore.FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)
