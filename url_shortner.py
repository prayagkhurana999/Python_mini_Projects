## url-> lengthy,shorten
from tkinter import *
from pyshorteners import *
def shorten():
    
    url=shortener()     #class in pyshorteners
    b=big.get()
    short_url=url.tinyurl.short(b)     #tinyurl is atribute in that short method is called
    small.insert(0,short_url)
    


master=Tk()
font_format=("helvatica","17","black,italic")
label1=label(master,text="Enter url",font=font_format).grid(row=0,coloumn=0)
label2=label(master,text="you short one",font=font_format).grid(row=1,coloumn=0)
button1=button(master,text="shortner",command=shorten,padx=40,pady=20).grid(row=2,coloumn=0)
big=Entry(master)
small=Entry(master)

big.grid(row0,coloumn=1,ipadx=20,ipady=20)
small.grid(row=1,coloumn=1)

master.mainloop()

