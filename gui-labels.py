from tkinter import *

window = Tk()

label = Label(window, text="Hello World", font=("Arial Bold", 25), foreground="blue", background="lightgrey", relief="solid",pady=10, padx=10, borderwidth=5, anchor="w")
label.pack()

window.mainloop()