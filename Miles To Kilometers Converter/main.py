from tkinter import *


def miles_to_km():
    user_input = mile_input.get()
    result = round(float(user_input) * 1.609)
    zero_label.config(text=str(result))


window = Tk()
window.title("Mile to KM Converter")
# window.minsize(width= 500, height= 300)
window.config(padx=20, pady=20)

mile_input = Entry(width=7)
mile_input.insert(END, string="0")
mile_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

zero_label = Label(text="0")
zero_label.grid(column=1, row= 1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command= miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()