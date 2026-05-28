import tkinter as tk
import random
from PIL import Image, ImageTk

windows = tk.Tk()
windows.overrideredirect(True)
windows.wm_attributes("-topmost",True)
windows.config(bg = "black")
windows.wm_attributes("-transparentcolor","black")
windows.title("Cat")
windows.geometry("300x300+1200+400")

cute_msgs = [
    "Hellooo",
    "Pet me",
    "Missed you"
]
angry_msgs = [
    "Iam hungry",
    "let me sleep",
    "Leave me alone"
]

def close_window(event):
    windows.destroy()

def cute_cat(event):
    left_click = random.choice(cute_msgs)
    message.config(text = left_click)
    cat_img.config(image = cat_img1)

def angry_cat(event):
    right_click = random.choice(angry_msgs)
    message.config(text = right_click)
    cat_img.config(image = cat_img2)


cat_img1 = Image.open("cat.png")
cat_img1 = cat_img1.resize((200,200))
cat_img1 = ImageTk.PhotoImage(cat_img1)

cat_img2 = Image.open("cat2.png")
cat_img2 = cat_img2.resize((250,250))
cat_img2 = ImageTk.PhotoImage(cat_img2)

cat_img = tk.Label(windows, image = cat_img1, bg = "black")
cat_img.pack()

random_msg = random.choice(cute_msgs)
message = tk.Label(windows,text = random_msg, bg = "black", fg = "white")
message.pack()

cat_img.bind("<Button-1>",cute_cat)
cat_img.bind("<Button-3>",angry_cat)
windows.bind("<Escape>",close_window)


windows.mainloop()