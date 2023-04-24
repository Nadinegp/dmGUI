
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\admin\Downloads\Projects\GUI\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("312x555")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#D9D9D9",
    height = 555,
    width = 312,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    312.1875,
    555.0,
    fill="#D9D9D9",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    155.0,
    102.0,
    image=image_image_1
)

canvas.create_rectangle(
    0.0,
    308.0,
    314.0,
    555.1199951171875,
    fill="#FFFFFF",
    outline="")
window.resizable(False, False)
window.mainloop()