
import requests
import json


GetJoke = requests.get('http://api.chucknorris.io/jokes/random')
GetJokeDict = json.loads(GetJoke.text)
print(GetJokeDict["value"])
