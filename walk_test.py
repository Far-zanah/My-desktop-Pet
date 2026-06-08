import tkinter as tk
from PIL import Image, ImageTk

windows = tk.Tk()
windows.geometry("300x300+1000+300")
windows.overrideredirect(True)
windows.wm_attributes("-topmost",True)
windows.title("WalkingCat")
windows.wm_attributes("-transparentcolor","black")
windows.config(bg = "black")

walking_frames = []
for i in range(6):
    filename = f"walk{i+1}.png"
    walk_img = Image.open(filename)
    walk_img = walk_img.resize((250,250))
    walk_img = ImageTk.PhotoImage(walk_img)
    walking_frames.append(walk_img)
current_img = 0
walk = tk.Label(windows, image = walking_frames[current_img], bg ="black")
walk.pack()
counter = 0
def animate():
    global counter
    counter = counter + 1
    walking_frames[counter]
    if counter == 5:
        counter = 0
    walk.config(image = walking_frames[counter])
    windows.after(100,animate)
animate()



windows.mainloop()
