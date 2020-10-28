import requests
from tkinter import *
from tkinter import messagebox
response=requests.get("enter the url here ")   #get is the inbult method of requests
data=response.json()
## here type(data) is  list 
##if we write data[0]["key"] it will give value
master=Tk()
button1=button(master,text="Generate",command=fetch()).grid(row=1,coloumn=0,columnspan=2)
label1=label(master,text="Quotes Application",font=("Arial",17,"black")).grid(row=0,coloumn=0)
i=0
def fetch():
    global data       #bcoz data is defined outside  
    global i
    text=data[i]["text"]
    author=data[i]["author"]
    messagebox.showinfo(author,text)
    i=i+1
    
master.mainloop()    
