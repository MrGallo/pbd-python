import random


player = {
    "name": "Awesome-Sauce",
    "health": 50,
    "strength": 20
}

damage_taken = random.randrange(10, 25)
print(f"Enemy hits {player['name']} for {damage_taken} damage.")
# subtract the player's health by the damage_taken variable

print()
print(f"Player: {player['name']}")
print(f"Health: {player['health']}")
print()
