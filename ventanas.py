import PySimpleGUI as sg
from PIL import Image

# Test

def crearVentanaArbol(path: str, tipo: str):

    im = Image.open(path)
    width, height = im.size

    anchoMayor = False
    altoMayor = False

    sg.theme("DarkAmber")
    layout = [[]]
    ventana = sg.Window("Árbol de expansión " + tipo, layout, margins = (0, 0), location = (0, 0), resizable = False, finalize = True)

    max_width, max_height = ventana.get_screen_size()
    max_width = int(max_width - 50)
    max_height = int(max_height * 0.9)

    if width > max_width:
        width = max_width
        anchoMayor = True
        height = height + 35
    if height > max_height:
        altoMayor = True
        width = width + 35
        height = max_height

    col = [[sg.Image(source = path)]]
    ventana = ventana.extend_layout(container = ventana, rows = [[sg.Column(col, scrollable = (anchoMayor or altoMayor), vertical_scroll_only = not anchoMayor)]])
    ventana.size = (width, height)
    ventana.refresh()

    return ventana