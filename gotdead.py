from pprint import pprint
from characters import characters

dead = 0
for character in characters:
    if character["died"] != "":
        dead += 1
print(dead)