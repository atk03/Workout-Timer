#atk03

from tkinter import *

root = Tk()


def message(ready, work, rest, n):

    to_return = []

    for i in range(int(ready)):
        to_return.append('Get Ready! \n' + str(i))
    to_return.append('')

    for i in range(int(n)):
        for ii in range(int(work)):
            to_return.append('Round: \n' + str(i) + '\n Work : \n' + str(ii))
        to_return.append('')
        for iii in range(int(rest)):
            to_return.append('Round: \n' + str(i) + '\n Rest : \n' + str(iii))
        to_return.append('')
    to_return.append('Good job! \n')
    return to_return


def return_val():

    work = e1.get()
    rest = e2.get()
    ready = e3.get()
    n = e4.get()

    msg = message(ready, work, rest, n)

    for m in msg:
        if m:
            result = t_label.config(text=m)
            root.after(1000, result)
            root.update()
        else:
            root.bell()


root.title('Timer')
root.iconbitmap("gloves.ico")
root.geometry("240x210")
root.resizable(0, 0)


w_label = Label(root, text="work (s)", font="Helvetica 12")
r_label = Label(root, text="rest (s)", font="Helvetica 12")
g_label = Label(root, text="get ready (s)", font="Helvetica 12")
n_label = Label(root, text='intervals', font="Helvetica 12")
t_label = Label(root)


panel = Label(root)
panel.grid(column=0, row=0, rowspan=11, columnspan=3)

w_label.grid(row=1, column=4)
r_label.grid(row=2, column=4)
g_label.grid(row=3, column=4)
n_label.grid(row=4, column=4)

t_label.grid(row=7, column=4, columnspan=2, rowspan=2)

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)

e1.grid(row=1, column=5)
e2.grid(row=2, column=5)
e3.grid(row=3, column=5)
e4.grid(row=4, column=5)


button3=Button(text='START', font="Helvetica 14 bold", command=return_val)
button3.grid(row=13, column=4)

button4=Button(text='STOP', font="Helvetica 14 bold", command=root.quit)
button4.grid(row=13, column=5)


mainloop()
