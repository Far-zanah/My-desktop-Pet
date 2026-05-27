import tkinter as tk
import random
from PIL import Image, ImageTk
windows = tk.Tk()
windows.title("BlackCat.exe")
windows.geometry("300x300")
cute_msgs = [
    "Hydrate NOW!",
    "Are you about to binge another show again?",
    "I missed you.",
    "You are perfect" 
    ]
angry_msgs =[
    "Pet me NOW!",
    "I am hungry, feed me NOW!",
    "I am bored, play with me NOW!",
    "Let me sleep."
    ]

def cute_message(event):
    left_message = random.choice(cute_msgs)
    message.config(text = left_message)
    cat_label.config(image = cat_img1 )
def angry_message(event):
    right_messages = random.choice(angry_msgs)
    message.config(text = right_messages)
    cat_label.config(image = cat_img2)

cat_img1 = Image.open("cat.png")
cat_img1 = cat_img1.resize((200, 200))
cat_img1 = ImageTk.PhotoImage(cat_img1)

cat_img2 = Image.open('cat2.png')
cat_img2 = cat_img2.resize((250,250))
cat_img2 = ImageTk.PhotoImage(cat_img2)

cat_label = tk.Label(windows, image=cat_img1)
cat_label.pack()

cat_label.bind("<Button-1>",cute_message)
cat_label.bind("<Button-3>", angry_message)

random_message = random.choice(cute_msgs)
message = tk.Label(windows, text=random_message)
message.pack()

windows.mainloop()