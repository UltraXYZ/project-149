from tkinter import *
import random

root = Tk()
root.title("Random Words")
root.geometry("400x400")

label1 = Label(root)
alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def word():
    r1 = random.randint(0,25)
    r2 = random.randint(0,25)
    r3 = random.randint(0,25)
    r4 = random.randint(0,25)
    r5 = random.randint(0,25)
    
    wr1 = alpha_list[r1]
    wr2 = alpha_list[r2]
    wr3 = alpha_list[r3]
    wr4 = alpha_list[r4]
    wr5 = alpha_list[r5]
    
    word = wr1 + wr2 + wr3 + wr4 + wr5
    print(word)
    label1["text"] = word
    
btn = Button(root, text="Click to make a random 5 Letter Word", command=word)
btn.place(relx=0.5, rely=0.45, anchor=CENTER)
label1.place(relx=0.5, rely=0.55, anchor=CENTER)

root.mainloop()