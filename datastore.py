import json
import os

class DataStore:
    FILE_NAME = "data.json"

    @staticmethod
    def load_data():
        # Load data if file exists
        if os.path.exists(DataStore.FILE_NAME):
            with open(DataStore.FILE_NAME, "r") as file:
                return json.load(file)
        
        # Default data structure
        return {"students": {}, "courses": {}}

    @staticmethod
    def save_data(data):
        # Save data to JSON file
        with open(DataStore.FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

