from cs50 import SQL

db = SQL("sqlite:///pokemons.db")

pokemon = input("Pokemon you want to search : ")

pokemons = db.execute("SELECT name FROM pokemons WHERE evolves_from = ?",pokemon)

print(pokemons)