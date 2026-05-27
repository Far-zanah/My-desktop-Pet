import tkinter as tk
import random
from PIL import Image, ImageTk

windows = tk.Tk()
windows.geometry ("300x300")
windows.title("BlackCat")

cute_msgs = [
    "Hellooo",
    "Hydrate Now",
    "Pet me"
]
angry_msgs = [ 
    "Let me sleep ",
    "Gimme Food",
    "leave me alone"
]
def cute_cat(event):
    left__messages = random.choice(cute_msgs)
    msg_label.config(text = left_messages)
    img_label.config(image = cute_img)

def angry_cat(event):
    right_messages = random.choice(angry_msgs)
    msg_label.config(text = right_messages)
    img_label.config(image = angry_img)

cute_img = Image.open("cat.png")
cute_img = cute_img.resize((200,200))
cute_img = ImageTk.PhotoImage(cute_img)

angry_img = Image.open("cat2.png")
angry_img = angry_img.resize((250,250))
angry_img = ImageTk.PhotoImage(angry_img)

img_label = tk.Label(windows, Image = angry_img)
img_label.pack()

random_message = random.choice(cute_msgs)
msg_label = tk.Label(windows, text = cute_msgs)
msg_label.pack()

img_label.bind("<Button-1",cute_cat)
img_label.bind("<Button-3>",angry_cat)
windows.mainloop()
