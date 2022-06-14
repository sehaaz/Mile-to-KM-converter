from tkinter import *

def calculate():
    miles = float(input.get())
    km = float(miles * 1.609)
    label3.config(text=km)

window = Tk()
window.title("Mile to KM converter")
window.minsize(width=300, height=200)

input = Entry(width=10)
input.grid(row=0, column=1)
miles = input.get()

label1 = Label(text="miles")
label1.grid(row=0, column=2)

label2 = Label(text="is equal to")
label2.grid(row=1, column=0)

km = 0

label3 = Label(text=km)
label3.grid(row=1, column=1)

label4 = Label(text="km")
label4.grid(row=1, column=2)

button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)




window.mainloop()