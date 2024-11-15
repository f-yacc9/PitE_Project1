import requests
import threading
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from configuration.config import ConfigManager
from configuration.logs import Logger

class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types

class PokemonManager:
    def __init__(self):
        self.config = ConfigManager.get_instance()
        self.logger = Logger(self.config.get("log_level"))
        self.pokemon_list = []
        self.lock = threading.Lock()

    
    def fetch_pokemon(self, name):
        url = f"https://pokeapi.co/api/v2/pokemon/{name}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            
            # Verifying the existence of types
            
            if "types" in data:
                types = [t["type"]["name"] for t in data["types"]]
                pokemon = Pokemon(name, types)
                with self.lock:
                    self.pokemon_list.append(pokemon)
                self.logger.log("INFO", f"Fetched {name} with types {types}")
            else:
                # if "types" is not there, the error is register
                self.logger.log("ERROR", f"Pokemon data for {name} missing 'types'")
        else:
            self.logger.log("ERROR", f"Failed to fetch {name} with status code {response.status_code}")
    
    
    
    
    def fetch_multiple_pokemon(self, names):
        threads = []
        max_threads = self.config.get("max_concurrent_requests")
        for name in names:
            if len(threads) >= max_threads:
                threads[0].join()
                threads.pop(0)
            thread = threading.Thread(target=self.fetch_pokemon, args=(name,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon_manager = PokemonManager()
        self.logger = Logger(ConfigManager.get_instance().get("log_level"))

    def search_and_store_pokemon(self, pokemon_names):
        self.logger.log("INFO", f"{self.name} is searching for Pokémon...")
        self.pokemon_manager.fetch_multiple_pokemon(pokemon_names)
        self.logger.log("INFO", f"{self.name} completed searching for Pokémon.")
