from pprint import pprint
from characters import characters


for character in characters:
    if character["name"][0] == "Z":
        print(character["name"])
    if character["name"][0].startswith("Z") == True:
        print(character["name"])
        