from tkinter import *


window=Tk()

def weight_converter():
    print("change")
    weight=float(entry.get())
    t2.insert(END, weight*1000)
    t4.insert(END, weight*2.20462)
    t6.insert(END, weight*35.274)

bt=Button(window, text="Convert", command=weight_converter)
bt.grid(row=0,column=0)

entry=StringVar()
entry=Entry(window,textvariable=entry)
entry.grid(row=0, column=2)

t1=Label(window, text="gram")
t1.grid(row=0, column=3)
t2=Text(window,height=2, width=20)
t2.grid(row=0, column=4)

t3=Label(window, text="pounds")
t3.grid(row=1, column=3)
t4=Text(window,height=2, width=20)
t4.grid(row=1, column=4)

t5=Label(window, text="ounce")
t5.grid(row=2, column=3)
t6=Text(window,height=2, width=20)
t6.grid(row=2, column=4)

window.mainloop()