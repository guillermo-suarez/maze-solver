import PySimpleGUI as sg
from PIL import Image

def crearVentanaArbol(path: str, tipo: str):

    im = Image.open(path)
    width, height = im.size

    max_width, max_height = 1875, 975

    if width > max_width:
        width = max_width
    if height > max_height:
        height = max_height

    sg.theme("DarkAmber")

    col = [[sg.Image(source = path)]]
    layout = [[sg.Column(col, size = (width, height), scrollable = True)]]
    ventana = sg.Window("Árbol de expansión" + " " + tipo, layout, margins = (0, 0), location = (0, 0), resizable = False, finalize = True)

    return ventana