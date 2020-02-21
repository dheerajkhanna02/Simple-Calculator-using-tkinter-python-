from tkinter import *
root= Tk()
root.title("Simple Calculator")

e=Entry(root,width=50,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))
def button_clear():
    e.delete(0,END)
def button_add():
    first_number=e.get()
    global f_num
    global math
    math="Addition"
    f_num=int(first_number)
    e.delete(0,END)
def button_equal():
    second_number=e.get()
    e.delete(0,END)
    if(math=="Addition"):
        e.insert(0,f_num + int(second_number))
    if(math=="Subtraction"):
        e.insert(0,f_num - int(second_number))
    if(math=="Multiplication"):
        e.insert(0,f_num * int(second_number))
    if(math=="Division"):
        e.insert(0,f_num / int(second_number))
        
def button_sub():
    first_number=e.get()
    global f_num
    global math
    math="Subtraction"
    f_num=int(first_number)
    e.delete(0,END)
def button_mul():
    first_number=e.get()
    global f_num
    global math
    math="Multiplication"
    f_num=int(first_number)
    e.delete(0,END)
def button_div():
    first_number=e.get()
    global f_num
    global math
    math="Division"
    f_num=int(first_number)
    e.delete(0,END)
    
    
    


B1=Button(root,text="1",command=lambda: button_click(1),padx=40,pady=20)
B2=Button(root,text="2",command=lambda: button_click(2),padx=40,pady=20)
B3=Button(root,text="3",command=lambda: button_click(3),padx=40,pady=20)
B4=Button(root,text="4",command=lambda: button_click(4),padx=40,pady=20)
B5=Button(root,text="5",command=lambda: button_click(5),padx=40,pady=20)
B6=Button(root,text="6",command=lambda: button_click(6),padx=40,pady=20)
B7=Button(root,text="7",command=lambda: button_click(7),padx=40,pady=20)
B8=Button(root,text="8",command=lambda: button_click(8),padx=40,pady=20)
B9=Button(root,text="9",command=lambda: button_click(9),padx=40,pady=20)
B0=Button(root,text="0",command=lambda: button_click(0),padx=40,pady=20)

B_add=Button(root,text="+",command=button_add,padx=40,pady=20)
B_sub=Button(root,text="-",command=button_sub,padx=40,pady=20)
B_mul=Button(root,text="*",command=button_mul,padx=40,pady=20)
B_div=Button(root,text="/",command=button_div,padx=40,pady=20)
B_equal=Button(root,text="=",command=button_equal,padx=80,pady=20)
B_clear=Button(root,text="Clear",command=button_clear,padx=40,pady=20)

#put buttons on the screen

B1.grid(row=3,column=0)
B2.grid(row=3,column=1)
B3.grid(row=3,column=2)

B4.grid(row=2,column=0)
B5.grid(row=2,column=1)
B6.grid(row=2,column=2)

B7.grid(row=1,column=0)
B8.grid(row=1,column=1)
B9.grid(row=1,column=2)

B0.grid(row=4,column=0)
B_add.grid(row=4,column=1)
B_clear.grid(row=4,column=2)

B_sub.grid(row=5,column=0)
B_mul.grid(row=5,column=1)
B_div.grid(row=5,column=2)

B_equal.grid(row=6,column=1,columnspan=2)
root.mainloop()
