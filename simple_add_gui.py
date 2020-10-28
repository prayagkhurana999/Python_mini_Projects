from tkinter import *
from tkinter import messagebox

master=Tk()

font_format=("Helvetica",17,"bold italic")  # this contain arugemts as family,size and type respectivle

label1=label(master,text="Enter number 1 :",font=font_format)
label2=label(master,text="Enter number 2 :",font=font_format)
num1=Entry(master)
num2=Entry(master)   #this entry is same as input

button1=button(master,text="add",font=font_format)
button2=button(master,text="exit",font=font_format)

label1.grid(row=0,coloumn=0)          ##here we dont use pack because it will occupy whole space so thats y we have taken grid
label2.grid(row=1,coloumn=0)

num1.grid(row=0,coloumn=1)
num2.grid(row=1,coloumn=1)

button1.grid(row=2,coloumn=0,columnsoan=2,padx=40,pady=20,command=add)   #here we can also take coloumnspan and rowspan  and padding like paddy alse
button2.grid(row=2,coloumn=1,columnsoan=2,padx=20,pady=20,command=master.quit) #quit is inbult function  #here command call for a function that will be automatically when button will clicled

master.mainloop()


def add():
    try:
     x=int(num1.get())    #to get the entry of user it will give in string by default
     y=int(num2.get())
     result=x+y
     messagebox.showinfo("Solution","the answer is {}".format(str(result)))
    except:
     messagebox.showerror("Error!, the value is invalid")    