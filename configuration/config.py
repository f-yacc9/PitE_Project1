class ConfigManager:
    _instance = None

    def __init__(self):
        if ConfigManager._instance is None:
            self.config = {
                "language": "en",
                "max_concurrent_requests": 3,
                "log_level": "INFO",
                "pokemon_type_filter": "all",
                "save_favorites": True
            }
            ConfigManager._instance = self
        else:
            raise Exception("ConfigManager is a singleton!")

    @staticmethod
    def get_instance():
        if ConfigManager._instance is None:
            ConfigManager()
        return ConfigManager._instance

    def get(self, key):
        return self.config.get(key)

    def set(self, key, value):
        self.config[key] = value
