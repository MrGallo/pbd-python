import json


with open("country-by-capital-city.json", 'r') as f:
    country_capitals = json.load(f)


for country in country_capitals:
    print(country)

