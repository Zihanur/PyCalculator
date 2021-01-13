from tkinter import *

a = Tk()
a.title("Calculator")
text_input = StringVar()
operator = ""
e = Entry(a,font=('arial',20,'bold'),bd=30,borderwidth=8,insertwidth=4,justify='right',textvariable=text_input).grid(row=0,column=0,columnspan=4)


def clickbtn(numbers):
    global operator
    operator=operator+str(numbers)
    text_input.set(operator)
def clrbtn():
    global operator
    operator=""
    text_input.set("")
def eqlbtn():
    global operator
    s=str(eval(operator))
    text_input.set(s)

btn7 = Button(a,text="7",font=('arial',20,'bold'),bd=8,padx=16,pady=16,command=lambda:clickbtn(7)).grid(row=1,column=0)
btn8 = Button(a,text="8",font=('arial',20,'bold'),bd=8,padx=16,pady=16,command=lambda:clickbtn(8)).grid(row=1,column=1)
btn9 = Button(a,text="9",font=('arial',20,'bold'),bd=8,padx=16,pady=16,command=lambda:clickbtn(9)).grid(row=1,column=2)
btn_dev = Button(a,text="/",font=('arial',20,'bold'),bg='red',bd=8,padx=16,pady=16,command=lambda:clickbtn("/")).grid(row=1,column=3)

btn4 = Button(a,text="4",font=('arial',20,'bold'),bd=8,padx=16,pady=16,command=lambda:clickbtn(4)).grid(row=2,column=0)
btn5 = Button(a,text="5",font=('arial',20,'bold'),bd=8,padx=16,pady=16,command=lambda:clickbtn(5)).grid(row=2,column=1)
btn6 = Button(a,text="6",font=('arial',20,'bold'),bd=8,padx=16,pady=16,command=lambda:clickbtn(6)).grid(row=2,column=2)
btn_mul = Button(a,text="x",font=('arial',20,'bold'),bg='red',bd=8,padx=16,pady=16,command=lambda:clickbtn("*")).grid(row=2,column=3)

btn1 = Button(a,text="1",font=('arial',20,'bold'),bd=8,padx=16,pady=16,command=lambda:clickbtn(1)).grid(row=3,column=0)
btn2 = Button(a,text="2",font=('arial',20,'bold'),bd=8,padx=16,pady=16,command=lambda:clickbtn(2)).grid(row=3,column=1)
btn3 = Button(a,text="3",font=('arial',20,'bold'),bd=8,padx=16,pady=16,command=lambda:clickbtn(3)).grid(row=3,column=2)
btn_sub = Button(a,text="-",font=('arial',20,'bold'),bg='red',bd=8,padx=16,pady=16,command=lambda:clickbtn("-")).grid(row=3,column=3)

btn0 = Button(a,text="0",font=('arial',20,'bold'),bd=8,padx=16,pady=16,command=lambda:clickbtn(0)).grid(row=4,column=0)
btn_c = Button(a,text="c",font=('arial',20,'bold'),bd=8,padx=16,pady=16,command=lambda:clrbtn()).grid(row=4,column=1)
btn_e = Button(a,text="=",font=('arial',20,'bold'),bd=8,padx=16,pady=16,command=lambda:eqlbtn()).grid(row=4,column=2)
btn_add = Button(a,text="+",font=('arial',20,'bold'),bg='red',bd=8,padx=16,pady=16,command=lambda:clickbtn("+")).grid(row=4,column=3)


a.mainloop()