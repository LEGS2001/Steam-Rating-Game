import requests
import urllib

from bs4 import BeautifulSoup

num_paginas = 100
num_juego = 0

for num_pagina in range(1, num_paginas + 1):
    # Hacer una solicitud GET a la página web de Steam
    url = f"https://store.steampowered.com/search/?filter=popularnew&page={num_pagina}"
    page = requests.get(url)

    # Verificar si la solicitud tuvo éxito
    if page.status_code == 200:
        # Crear un objeto BeautifulSoup para parsear el contenido de la página web
        soup = BeautifulSoup(page.content, "html.parser")

        # Buscar todos los elementos que contienen información sobre los juegos
        games = soup.find_all("a", class_="search_result_row")

        # Imprimir información sobre cada juego
        for game in games:
            print(f"Se han adquirido {num_juego} juegos")

            titulo = game.find("span", class_="title").text
            titulo = titulo.replace(':','').replace('!','').replace('?','').replace('/','')
            link = game.find("img")['srcset'].split(",")[1].strip()[:-3]
            urllib.request.urlretrieve(link, f"./fotos/{titulo}.png")    

            num_juego += 1
    else:
        print("La solicitud no tuvo éxito.")
