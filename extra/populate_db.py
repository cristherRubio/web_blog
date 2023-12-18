import requests
import sqlite3

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=1500&offset=0").json()

db = sqlite3.connect("pokemon.db")
cur = db.cursor()

for pokemon in response["results"]:
    name = pokemon["name"]
    response_pk = requests.get(pokemon["url"]).json()
    artwork = response_pk["sprites"]["other"]["official-artwork"]["front_default"]
    types = ", ".join([t["type"]["name"] for t in response_pk["types"]])
    data = [name, types, artwork]
    cur.execute("INSERT INTO pokemon(name, types, img_url) VALUES(?, ?, ?);", data)
    db.commit()