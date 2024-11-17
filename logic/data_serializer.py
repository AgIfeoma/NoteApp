import json

class DataSerializer:
    @staticmethod
    def save_to_file(data, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    @staticmethod
    def load_from_file(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)