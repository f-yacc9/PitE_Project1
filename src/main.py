"""

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
"""


from trainer import Trainer
from configuration.config import ConfigManager

# Initial configuration
config = ConfigManager.get_instance()
config.set("max_concurrent_requests", 3)
config.set("log_level", "INFO")

print("\n******************************* WELCOME TO THE POKEMON TYPE ANALYSER *******************************\n")

# Configurate a Trainer
trainer_name = str(input("What's your name? -> "))
trainer_name = Trainer(trainer_name)

# Pokemons to look for
# pokemon_names = ["pikachu", "charmander", "bulbasaur", "squirtle", "eevee"]

pokemons = []

poke_name = str(input("What pokemon do you need to find? -> ")).lower()
conf = str(input("Do you want another one? (Y/N) \nPress ENTER if you don't want more\n-> ")).upper()

pokemons.append(poke_name)

if conf == "Y":
    while True:
        name = str(input("  -> "))
        pokemons.append(name)

        if name == "":
            pokemons = pokemons[:-1]  
            break

# Pokemon search and save
trainer_name.search_and_store_pokemon(pokemons)
