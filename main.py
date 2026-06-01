import tkinter as tk
import random
from PIL import Image, ImageTk

windows = tk.Tk()
windows.overrideredirect(True)
windows.wm_attributes("-topmost",True)
windows.config(bg ="black")
windows.wm_attributes("-transparentcolor","black")
windows.title("BlackCat.exe")
windows.geometry("300x300+1000+300")


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
sleepy_msgs = [
    "Iam sleepy",
    "Let me sleep",
    "iam tired"
]
def cute_mood():
    message.config(text = random.choice(cute_msgs))
    cat_label.config(image = cat_img1)
def angry_mood():
    message.config(text = random.choice(angry_msgs))
    cat_label.config(image = cat_img2)
def sleep_mood():
    message.config(text = random.choice(sleepy_msgs))
    cat_label.config(image = cat_img3, bg = "black")
def random_mood():
    mood = random.choice([cute_mood,angry_mood,sleep_mood])
    mood()
    windows.after(6000,random_mood)



#def random_mood():
 #   message.config(text = random.choice(cute_msgs))
  #  message.config(text = random.choice(angry_msgs))
   # windows.after(3000, random_mood)

def close_app(event):
    windows.destroy()
def cute_message(event):
    left_message = random.choice(cute_msgs)
    message.config(text = left_message)
    cat_label.config(image = cat_img1 )
def angry_message(event):
    right_messages = random.choice(angry_msgs)
    message.config(text = right_messages)
    cat_label.config(image = cat_img2, bg = "black")


cat_img1 = Image.open("cat.png")
cat_img1 = cat_img1.resize((200, 200))
cat_img1 = ImageTk.PhotoImage(cat_img1)
cat_img2 = Image.open('cat2.png')
cat_img2 = cat_img2.resize((215,215))
cat_img2 = ImageTk.PhotoImage(cat_img2)
cat_img3 = Image.open("cat3.png")
cat_img3 = cat_img3.resize((250,250))
cat_img3 = ImageTk.PhotoImage(cat_img3)


cat_label = tk.Label(windows, image=cat_img1, bg = "black")
cat_label.pack()


cat_label.bind("<Button-1>",cute_message)
cat_label.bind("<Button-3>", angry_message)


random_message = random.choice(cute_msgs)
message = tk.Label(windows, text = random_message, font = ("arial", 10, "bold"), bg ="black", fg = "white")
message.pack()
current_mood = "cute"

def pet_cat(event):
    global current_mood
    if  current_mood =="cute":
        current_mood ="sleepy" 
        sleep_mood()
    elif current_mood =="sleepy":
        current_mood = "angry" 
        angry_mood()
    elif current_mood =="angry":
        current_mood = "cute" 
        cute_mood()
cat_label.bind("<Button-1>",pet_cat)


random_mood()
windows.bind("<Escape>",close_app)

windows.mainloop()