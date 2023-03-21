import tkinter as tk
import random
from PIL import Image, ImageTk


window = tk.Tk()
window.geometry("500x360")
window.title("Dice Roll")

# def roll_dice():
#     a = random.randint(1,6)
#     label = tk.Label(window, text=a).pack()


# button = tk.Button(window,text = "click", command=roll_dice)
# button.pack()


dice = ["./images/1.jpg","./images/2.jpg","./images/3.jpg","./images/4.jpg","./images/5.jpg","./images/6.jpg"]
images = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label = tk.Label(window, image=images)

label.image= images

label.place(x=200 , y=120)

def dice_roll():
    images = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label.configure(image= images )
    label.image = images

    
button = tk.Button(window, text="ROLL",bg="green",fg="white",font="Times 20 bold",command="dice_roll")
button.place(x = 200 , y = 0)
window.mainloop()
