from tkinter import *

def calculate():
    print("calculate")
    miles = float(input.get())
    km = round(miles * 1.609,2)
    km_value_initial.config(text=str(km))

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=40, pady=20)

#Entry
input = Entry(width=10)
input.insert(END, string="0")
print(input.get())
input.grid(column=1, row=0)

#Label
miles = Label(text="Miles")
miles.grid(column=2, row=0)
miles.config(padx=5)

is_eq = Label(text="is equal to")
is_eq.grid(column=0,row=1)

km_value_initial = Label(text="0")
km_value_initial.grid(column=1,row=1)

km = Label(text="Km")
km.grid(column=2,row=1)
km.config(padx=10)

#Button
button = Button(text="Calculate",command=calculate)
button.grid(column=1,row=2)
window.mainloop()