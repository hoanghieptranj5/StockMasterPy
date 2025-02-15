import json


class ConfigManager:
    def __init__(self, config_file):
        self._config = self._load_config(config_file)

    @staticmethod
    def _load_config(config_file):
        try:
            with open(config_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f'Configuration file {config_file} not found.')
            raise
        except json.JSONDecodeError:
            print(f'Error decoding JSON in {config_file}.')
            raise

    def __getattr__(self, name):
        return self._config.get(name, None)

    def get(self, key, default=None):
        return self._config.get(key, default)
