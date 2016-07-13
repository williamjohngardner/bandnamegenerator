import random

def get_album_name():

    with open("faulkner.txt", "r") as outfile:
        faulkner = outfile.read().splitlines()

        album_name = random.choice(faulkner).title()

        print(album_name)


get_album_name()
