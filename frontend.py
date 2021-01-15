from tkinter import *

window = Tk()
l1 = Label(window, text="Roll")
l1.grid(row=0, column=0)

roll_value = StringVar()
e1 = Entry(window, textvariable=roll_value)
e1.grid(row=0, column=1)

l2 = Label(window, text="Name")
l2.grid(row=0, column=2)

name_value = StringVar()
e2 = Entry(window, textvariable=name_value)
e2.grid(row=0, column=3)

l3 = Label(window, text="DOB")
l3.grid(row=1, column=0)

dob_value = StringVar()
e3 = Entry(window, textvariable=dob_value)
e3.grid(row=1, column=1)

l4 = Label(window, text="Gender")
l4.grid(row=1, column=2)

gender_value = StringVar()
e4 = Entry(window, textvariable=gender_value)
e4.grid(row=1, column=3)

l1 = Text(window, height=6, width=35)
l1.grid(row=2, column=0, rowspan=6, columnspan=2)

s1 = Scrollbar(window)
s1.grid(row=2, column=2, rowspan=6)

# vertical scroll of yaxis set to this scroll i.e, s1

l1.configure(yscrollcommand=s1.set)

# configure the s1 so that the vertical view of the text changes with respect to this scroll

s1.configure(command=l1.yview)

b1 = Button(window, text="ViewAll", width=12)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search Entry", width=12)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add", width=12)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width=12)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete", width=12)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12)
b6.grid(row=7, column=3)

window.mainloop()
