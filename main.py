import tkinter as tk
import ttkbootstrap as ttk

from PIL import ImageTk, Image

import random, time, os

def elegirJuego1():
    ganadores.append(juego1)
    cargarJuegos()

def elegirJuego2():
    ganadores.append(juego2)
    cargarJuegos()

def cargarJuegos():
    global img1, img2, juego1, juego2, NUM_JUEGOS, participantes, ganadores

    if (len(ganadores) == NUM_JUEGOS):
        participantes = ganadores.copy()
        ganadores.clear()
        NUM_JUEGOS /= 2

    if NUM_JUEGOS < 1:
        print(f"El ganador es: {participantes[0].replace('png','')}")
        window.destroy()
        time.sleep(2)
        return

    juego1 = participantes.pop(random.randint(0, len(participantes) - 1))
    img1 = Image.open(f"fotos/{juego1}")
    img1 = ImageTk.PhotoImage(img1)
    img1_label.configure(image=img1) 

    juego2 = participantes.pop(random.randint(0, len(participantes) - 1))
    img2 = Image.open(f"fotos/{juego2}")
    img2 = ImageTk.PhotoImage(img2)
    img2_label.configure(image=img2) 

# el numero de juegos que clasifican la primera ronda
NUM_JUEGOS = 16

ganadores = []
participantes = []

# toma el numero de juegos que van a participar en la primera ronda
while (len(participantes) < (NUM_JUEGOS * 2)):
    participante = random.choice(os.listdir("fotos"))
    if participante not in participantes:
        participantes.append(participante)

juego1 = participantes.pop(random.randint(0, len(participantes) - 1))
juego2 = participantes.pop(random.randint(0, len(participantes) - 1))

# main
window = ttk.Window(themename="darkly") # hacer cambio entre darkly y journal
window.title("Steam Rating Game")
window.geometry = ("300x200")

# frame juego 1
game1_frame = tk.Frame(window)

# foto 1
img1 = ImageTk.PhotoImage(Image.open(f"fotos/{juego1}"))
img1_label = tk.Label(game1_frame, image=img1)
img1_label.pack(pady= 10)

# boton 1
button1 = tk.Button(game1_frame, text="Game 1", font="Arial 12", command=elegirJuego1)
button1.pack()

game1_frame.pack(side="left", pady= 20, padx=20)


# frame juego 2
game2_frame = tk.Frame(window)

# foto 2
img2 = ImageTk.PhotoImage(Image.open(f"fotos/{juego2}"))
img2_label = tk.Label(game2_frame, image=img2)
img2_label.pack(pady= 10)

# boton 2
button2 = tk.Button(game2_frame, text="Game 2", font="Arial 12", command=elegirJuego2)
button2.pack()

game2_frame.pack(side="left", pady= 20, padx=20)

tk.mainloop()