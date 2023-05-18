from tkinter import *
import time
from babel.numbers import *
from babel.dates import *

ck = Tk()
ck.title("Digital Clock")
ck.geometry("1200x600")
ck.maxsize(1200, 600)
ck.minsize(1200, 600)
ck.config(bg='#0000ff')
ck.iconbitmap("Apparky.ico")


def clock():
    h = str(time.strftime("%H"))
    m = str(time.strftime("%M"))
    s = str(time.strftime("%S"))
    #    print(h, m, s)
    if int(h) > 11 and int(m) > 0:
        lbl_n.config(text="PM")
    if int(h) > 12:
        h = str(int(int(h) - 12))

    lbl_h.config(text=h)
    lbl_m.config(text=m)
    lbl_s.config(text=s)
    lbl_h.after(500, clock)


lbl_h = Label(ck, text="12", font=("Times New Roman ", 55, 'bold'), bg="white", fg='black')
lbl_h.place(x=300, y=200, width=135, height=90)

lbl_h_t = Label(ck, text="HOUR", font=("Times New Roman ", 20, 'bold'), bg="white", fg='black')
lbl_h_t.place(x=300, y=320, width=135, height=60)

lbl_m = Label(ck, text="00", font=("Times New Roman ", 55, 'bold'), bg="white", fg='black')
lbl_m.place(x=450, y=200, width=135, height=90)

lbl_m_t = Label(ck, text="MINUITES", font=("Times New Roman ", 20, 'bold'), bg="white", fg='black')
lbl_m_t.place(x=450, y=320, width=135, height=60)

lbl_s = Label(ck, text="12", font=("Times New Roman ", 55, 'bold'), bg="white", fg='black')
lbl_s.place(x=600, y=200, width=135, height=90)

lbl_s_t = Label(ck, text="SECONDS", font=("Times New Roman ", 20, 'bold'), bg="white", fg='black')
lbl_s_t.place(x=600, y=320, width=135, height=60)

lbl_n = Label(ck, text="A.M", font=("Times New Roman ", 55, 'bold'), bg="white", fg='black')
lbl_n.place(x=750, y=200, width=135, height=90)

lbl_n_t = Label(ck, text="AM/PM", font=("Times New Roman ", 20, 'bold'), bg="white", fg='black')
lbl_n_t.place(x=750, y=320, width=135, height=60)

name_label = Label(ck, text="Powered by Apparky", font=("Times New Roman ", 20, 'bold'), bg="blue")
name_label.pack()

exit_button = Button(ck, text="Exit", command=ck.destroy, bg="blue")
exit_button.pack(anchor=SE, side=BOTTOM)

clock()

ck.mainloop()
