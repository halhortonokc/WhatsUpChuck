
import requests

GetJoke = requests.get('http://api.chucknorris.io/jokes/random')
Joke = GetJoke.json()
print(Joke["value"])
