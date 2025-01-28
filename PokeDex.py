import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None

print("Welcome To Jesal's Pokedex !!!")
print("----------------------")

pokemon_name = input("Enter a Pokémon name to get info: ")
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print("\n--- Pokémon Details ---")
    print(f"Name: {pokemon_info['name'].capitalize()}")
    print(f"ID: {pokemon_info['id']}")
    print(f"Height: {pokemon_info['height'] / 10} m")  # Converting to meters
    print(f"Weight: {pokemon_info['weight'] / 10} kg")  # Converting to kg
    print(f"Base Experience: {pokemon_info['base_experience']} XP")

    # Getting the abilities
    abilities = [ability["ability"]["name"].capitalize() for ability in pokemon_info["abilities"]]
    print(f"Abilities: {', '.join(abilities)}")

    # Getting the types
    types = [t["type"]["name"].capitalize() for t in pokemon_info["types"]]
    print(f"Types: {', '.join(types)}")

    # Getting the stats
    print("\n--- Stats ---")
    for stat in pokemon_info["stats"]:
        print(f"{stat['stat']['name'].capitalize()}: {stat['base_stat']}")

    # Getting Moves (Limiting to first 5 moves for brevity)
    moves = [move["move"]["name"].capitalize() for move in pokemon_info["moves"][:5]]
    print(f"\nMoves: {', '.join(moves)}...")  # Displaying first 5 moves

    # Getting Front Default Sprite
    print(f"\nSprite: {pokemon_info['sprites']['front_default']}")

    print("\n----------------------")
