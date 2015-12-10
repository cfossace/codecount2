from Tkinter import *
import ttk

root = Tk()

root.title("Check Box")
root.geometry("500x500")
app = Frame(root)
app.grid()

var = StringVar()
check = Checkbutton(app, text = "Yeah Kid", variable = var)
check.pack()




root.mainloop()
