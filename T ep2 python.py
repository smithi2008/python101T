import random
import tkinter as tk
from tkinter import messagebox
GUI = tk.Tk()
GUI.title('เล่นกีฬาอะไรดี?')
GUI.geometry('500x400')
def random_sport():
    sport = ["Basketball","Volley Ball","Tennis","Batminton","Soccor","Table Tennis","Hockeys","Swimming","Jogging","Fishing","Chess"]
    sport = random.choice(sport)
    text = sport
    messagebox.showinfo('วันนี้จะเล่น',text)
        
button = tk.Button(GUI,text='เล่นกีฬาอะไรดี?', font=("TkDefaultfont",20), command=random_sport)
button.place(x=210,y=200)

GUI.mainloop()
