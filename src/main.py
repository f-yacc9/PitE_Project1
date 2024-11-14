
import json

import requests

# base URL
"""poke_url = "https://pokeapi.co/api/v2/pokedex/1"



ENDPOINTS = [
    "ability",
    "berry",
    "berry-firmness",
    "berry-flavor",
    "characteristic",
    "contest-effect",
    "contest-type",
    "egg-group",
    "encounter-condition",
    "encounter-condition-value",
    "encounter-method",
    "evolution-chain",
    "evolution-trigger",
    "gender",
    "generation",
    "growth-rate",
    "item",
    "item-attribute",
    "item-category",
    "item-fling-effect",
    "item-pocket",
    "language",
    "location",
    "location-area",
    "machine",
    "move",
    "move-ailment",
    "move-battle-style",
    "move-category",
    "move-damage-class",
    "move-learn-method",
    "move-target",
    "nature",
    "pal-park-area",
    "pokeathlon-stat",
    "pokedex",
    "pokemon",
    "pokemon-color",
    "pokemon-form",
    "pokemon-habitat",
    "pokemon-shape",
    "pokemon-species",
    "region",
    "stat",
    "super-contest-effect",
    "type",
    "version",
    "version-group"
    ]

# Realiza la solicitud GET
response = requests.get(poke_url)

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    # Imprime el contenido de la respuesta en formato JSON
    data = response.json()
    print("Recursos disponibles:")
    for key, value in data.items():
        print(f"{key}: {value}")
    for key, value in data.items():
        # Imprime el nombre del recurso y su URL con indentación
        print(f"{key.capitalize()}: {value}\n")
        
else:
    print("Error al acceder a la API:", response.status_code)
"""

# main.py
from trainer import Trainer
from configuration.config import ConfigManager

# Initial configuration
config = ConfigManager.get_instance()
config.set("max_concurrent_requests", 3)
config.set("log_level", "INFO")

# Configurate a Trainer
trainer = Trainer("Maria")

# Pokemons to look for
pokemon_names = ["pikachu", "charmander", "bulbasaur", "squirtle", "eevee"]

# Pokemon search and save
trainer.search_and_store_pokemon(pokemon_names)
