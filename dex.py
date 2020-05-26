import requests
import urllib.request
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from gtts import gTTS
import os

while(1):
    poke = input("\n\nPlease enter a Pokemon name or dex number:")
    if (poke == "quit") | (poke == "Quit"):
        print("\n")
        quit()

    url = "https://pokeapi.co/api/v2/pokemon-species/" + poke
    info = requests.get(url)

    url2 = "https://pokeapi.co/api/v2/pokemon/" + poke
    info2 = requests.get(url2)

    try:
        print("\n" + info.json()["name"].capitalize() + ":\n")
    except:
        print("Pokemon could not be found")
        quit()

    foundEntry = 0
    for text in info.json()["flavor_text_entries"]:
        if (text['language']['name'] == 'en') & (foundEntry == 0):
            dexText = text['flavor_text']
            print(dexText.rstrip("\n") + "\n")
            foundEntry = 1

    speech = gTTS(dexText.replace("\n", " "), lang='en')
    speech.save("dexText.mp3")
    os.system("start dexText.mp3")

    try:
        urllib.request.urlretrieve(info2.json()["sprites"]["front_default"], "pokeSprite.png")

        img = mpimg.imread('pokeSprite.png')
        imgPlot = plt.imshow(img)
        plt.show()
    except:
        print("Could not find image")

    print("\nType quit to exit the program")



