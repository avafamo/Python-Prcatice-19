from tkinter import *

root = Tk()
root.title("button")
root.geometry('400x300')
root.resizable(width=False, height=False)

my_name = StringVar()


def print_my_name():
    my_name.set('my name is Mohammad')


btn = Button(root, text="show my name!", command=lambda: print_my_name())
btn.place(x=10, y=10)

label = Label(root, textvariable=my_name)
label.place(x=10, y=50)

root.mainloop()
