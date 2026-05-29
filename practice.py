import tkinter as tk
import random
from PIL import Image, ImageTk

windows = tk.Tk()
windows.overrideredirect(True)
windows.title("BlackCat")
windows.geometry("300x300+1000+300")
windows.wm_attributes("-topmost",True)
windows.config(bg="black")
windows.wm_attributes("-transparentcolor","black") 

cute_msg = [ 
    "Pet me",
    "Helloo",
    "Hydrate now"
]
angry_msg = [
    "Leave me alone",
    "Iam hungry",
    "Pay me attenton"
]
sleepy_msg =[
    "Let me sleep",
    "Iam tired",
    "Yawn.."
]

def cute_mood():
    message.config(text = random.choice(cute_msg))
    cat_img.config(image = cat_img1)
def angry_mood():
    message.config(text = random.choice(angry_msg))
    cat_img.config (image = cat_img2 )
def sleepy_mood():
    message.config(text = random.choice(sleepy_msg))
    cat_img.config(image = cat_img3)

def cat_mood():
    mood = random.choice([cute_mood,angry_mood,sleepy_mood])
    mood()
    windows.after(3000,cat_mood)
    
def close_app(event):
    windows.destroy()

message = random.choice(cute_msg)
message = tk.Label(windows, text = message, bg = "black", fg = "white")
message.pack()
cat_img1 = Image.open("cat.png")
cat_img1 = cat_img1.resize((250,250))
cat_img1 = ImageTk.PhotoImage(cat_img1)
cat_img2 = Image.open("cat2.png")
cat_img2 = cat_img2.resize((250,250))
cat_img2 = ImageTk.PhotoImage(cat_img2)
cat_img3 = Image.open("cat3.png")
cat_img3 = cat_img3.resize((250,250))
cat_img3 = ImageTk.PhotoImage(cat_img3)
cat_img = tk.Label(windows, image = cat_img1, bg = "black")
cat_img.pack()

windows.bind("<Escape>",close_app)
cat_mood()

windows.mainloop()
