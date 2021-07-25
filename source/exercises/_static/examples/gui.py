from tkinter import *


def handle_submit():
    print(f"Name: {entry_name.get()}")
    print(f"Age: {entry_age.get()}")


root = Tk()
frame = Frame(root)
label_name = Label(frame, text="Your Name:")
label_age = Label(frame, text="Your Age:")
entry_name = Entry(frame)
entry_age = Entry(frame)
button_submit = Button(frame, text="Submit", command=handle_submit)

frame.grid()
label_name.grid(column=0, row=0)
label_age.grid(column=0, row=1)
entry_name.grid(column=1, row=0)
entry_age.grid(column=1, row=1)
button_submit.grid(row=2, columnspan=2)

root.mainloop()


