from datetime import date as d
def sub():
    try:
        year=int(t1.get())
        month=int(t2.get())
        date=int(t3.get())
        dob=d(year,month,date)
        td=d.today()
        if dob.year>td.year or year<0 or dob.month>12 or dob.day>31:
            raise ValueError
        age=td.year-dob.year-((td.month,td.day)<(dob.month,dob.day))
        l.configure(text=str(age)+' years old',font=('bold'),bg='green')
    except ValueError:
        l.configure(text='Enter Dates Correctly',bg='red',font=('bold'))
def clr():
    l.configure(text='',bg='light green')
    t1.delete(0,len(t1.get()))
    t2.delete(0,len(t2.get()))
    t3.delete(0,len(t3.get()))
def bsy():
    l.configure(text='')
    s=t1.get()
    s=s[:-1]
    t1.delete(0,len(t1.get()))
    t1.insert(0,s)
def bsm():
    l.configure(text='')
    s=t2.get()
    s=s[:-1]
    t2.delete(0,len(t1.get()))
    t2.insert(0,s)
def bsd():
    l.configure(text='')
    s=t3.get()
    s=s[:-1]
    t3.delete(0,len(t1.get()))
    t3.insert(0,s)
from tkinter import *
w=Tk()
w.geometry('600x125')
w.title("Dhanush's age calculator")
w.configure(bg='light green')
l1=Label(w,text='Enter Your Birth Year',width=20,bg='light blue')
l1.grid(row=0,column=0)
l2=Label(w,text='Enter Your Birth Month',width=20,bg='light pink')
l2.grid(row=1,column=0)
l3=Label(w,text='Enter Your Birth Date',width=20,bg='light yellow')
l3.grid(row=2,column=0,columnspan=1)
t1=Entry(w,width=50)
t1.grid(row=0,column=1)
t2=Entry(w,width=50)
t2.grid(row=1,column=1)
t3=Entry(w,width=50)
t3.grid(row=2,column=1)
clrb=Button(w,text='Clear',command=clr,height=4,width=6,bg='red')
clrb.grid(row=0,column=3,rowspan=3)
bsyb=Button(w,text='<|--',command=bsy,bg='light blue')
bsyb.grid(row=0,column=2)
bsmb=Button(w,text='<|--',command=bsm,bg='light pink')
bsmb.grid(row=1,column=2)
bsdb=Button(w,text='<|--',command=bsd,bg='light yellow')
bsdb.grid(row=2,column=2)
subb=Button(w,text='Submit',command=sub,height=4,width=6,bg='green')
subb.grid(row=0,column=4,rowspan=3)
l=Label(w,text='',bg='light green')
l.grid(row=4,column=0,columnspan=5)
