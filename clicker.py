from tkinter import *

win = Tk()
win.title('DNS progs')
win.geometry('300x300')
win['bg'] = 'black'
label = Label(win, text='0', font=('arial', 100), fg='white', bg='black')
label_END = Label(win, text='9999', font=('arial', 100), fg='white', bg='black')
label.pack()
count = 0


def clicked():
    global count
    count += 1
    label.configure(text=count)
    if count < 10:
        label.place(x=115, y=10)
    elif count < 100:
        label.place(x=70, y=10)
    elif count < 1000:
        label.place(x=35, y=10)
    elif count < 9999:
        label.place(x=1, y=10)
    else:
        label_END.place(x=1, y=10)


btn = Button(win, text='Clicked', font=('arial', 30), border=True, padx=30, command=clicked)
btn.place(x=45, y=170)
win.mainloop()