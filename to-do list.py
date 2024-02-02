from tkinter import *
from tkinter import messagebox
window= Tk()
window.geometry("700x700")
window.title("to-do list")
def submit():
    item=data.get()
    lst.insert(END,item)
    messagebox.showinfo("message","submited successfully")
    data.delete(0,END)
def lstbind(event):
    id=lst.curselection()
    data=lst.get(id)
    mdata.set(data)
def edit():
    if(data.get() != ""):
        uid=lst.index(ANCHOR)
        udata=data.get()
        lst.delete(ANCHOR)
        lst.insert(uid,udata)
        messagebox.showinfo("message","edited successfully")
        data.delete(0,END) 
    else:
        messagebox.showinfo("message","please select any option")  
def delete():
    lst.delete(ANCHOR)
    data.delete(0,END)  
def deleteall():
    for item in reversed(lst.curselection()):
        lst.delete(item)  
        data.delete(0,END)          
lb=Label(window,text="to-do list",bg="#2c3e50",fg="white",padx=100,pady=30,font=("times",15,"bold"))
lb.grid(padx=40,row=0,column=0)
txt=Label(window,text="add items",font=("times",15,"bold"))
txt.grid(row=1,column=0)
mdata=StringVar()
data=Entry(window,width=40,textvariable=mdata)
data.grid(row=1,column=1)
bl=Label(window,text="added items",font=("times",15,"bold"))
bl.grid(row=2,column=0)
lst=Listbox(window,width=40,height=15,selectmode=EXTENDED)
lst.grid(row=2,column=1)
lst.bind("<<ListboxSelect>>",lstbind)
btsub=Button(window,text="submit",padx=20,pady=10,width=10,bg="#16a085",fg="white",font=("times",15,"bold"),command=submit)
btsub.grid(row=3,column=0)
btsel=Button(window,text="edit",padx=20,pady=10,width=10,bg="orange",fg="white",font=("times",15,"bold"),command=edit)
btsel.grid(row=3,column=1)
btdel=Button(window,text="delete",padx=20,pady=10,width=10,bg="red",fg="white",font=("times",15,"bold"),command=delete)
btdel.grid(row=4,column=0)
aldel=Button(window,text="delete all",padx=20,pady=10,width=10,bg="red",fg="white",font=("times",15,"bold"),command=deleteall)
aldel.grid(row=4,column=1)

window.mainloop()