
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from PIL import Image, ImageTk
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\admin\Downloads\Projects\GUI\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("315x555")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 555,
    width = 315,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    1.0,
    0.0,
    313.1875,
    555.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    119.0,
    70.0,
    anchor="nw",
    text="Credit 9.0",
    fill="#8FAF20",
    font=("Arial BoldMT", 16 * -1)
)

image_path = relative_to_assets("gb.png")
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
button_2 = Label(window, image=photo)

button_2.place(
    x=176.81549072265625,
    y=206.95050048828125,
    width=86.91655731201172,
    height=28.78765106201172
)

button_image_2 = PhotoImage(
    file=relative_to_assets("confirm.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=46.16387939453125,
    y=206.95050048828125,
    width=86.91655731201172,
    height=28.78765106201172
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    63.14642333984375,
    146.15866088867188,
    image=image_image_1
)

canvas.create_rectangle(
    96.54235994815826,
    144.94629061222076,
    185.11974334716797,
    146.60711669921875,
    fill="#515F1F",
    outline="")

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    233.26397705078125,
    145.48037719726562,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    155.0,
    25.0,
    image=image_image_3
)

canvas.create_rectangle(
    1.0,
    308.0,
    315.0,
    555.1199951171875,
    fill="#FFFFFF",
    outline="")

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=9.0,
    y=9.0,
    width=47.0,
    height=23.0
)
window.resizable(False, False)
window.mainloop()
