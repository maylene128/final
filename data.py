from tkinter import *

window = Tk()

window.title("Eagle Technology Client")

window.geometry('350x200')

lblF = Label(window, text="First Name")

lblF.grid(column=0, row=0)

txtF = Entry(window,width=10)

txtF.grid(column=1, row=0)
lblL = Label(window, text="Last Name")

lblL.grid(column=0, row=1)

txtL = Entry(window,width=10)

txtL.grid(column=1, row=1)

lblZ = Label(window, text="Zip Code")

lblZ.grid(column=0, row=2)

txtZ = Entry(window,width=10)

txtZ.grid(column=1, row=2)
lblP = Label(window, text="Phone Number")

lblP.grid(column=0, row=3)

txtP = Entry(window,width=10)

txtP.grid(column=1, row=3)

def clicked():

        f = open("EagleTechnology.txt", "a")

        res = "Thank you! Your information was saved."
        lblF.configure(text= res)
        lblL.configure(text="")
        lblZ.configure(text="")
        lblP.configure(text="")
        f.write("\n" + txtF.get() + ", " + txtL.get() + ", " + txtP.get() + ", " + txtZ.get())
        txtF.destroy()
        txtL.destroy()
        txtP.destroy()
        txtZ.destroy()
        btn.destroy()
        f.close()
btn = Button(window, text="Enter", command=clicked)
btn.grid(column=2, row=3)

window.mainloop()
