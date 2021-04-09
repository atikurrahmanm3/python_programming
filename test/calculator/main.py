import tkinter
from tkinter import *
from tkinter import messagebox

#variables
val =""
A = 0
operator = ""

#functions
def btn1_is_clicked():
    global val
    val = val + "1"
    data.set(val)

def btn2_is_clicked():
    global val
    val = val + "2"
    data.set(val)

def btn3_is_clicked():
    global val
    val = val + "3"
    data.set(val)

def btn4_is_clicked():
    global val
    val = val + "4"
    data.set(val)

def btn5_is_clicked():
    global val
    val = val + "5"
    data.set(val)

def btn6_is_clicked():
    global val
    val = val + "6"
    data.set(val)

def btn7_is_clicked():
    global val
    val = val + "7"
    data.set(val)

def btn8_is_clicked():
    global val
    val = val + "8"
    data.set(val)

def btn9_is_clicked():
    global val
    val = val + "9"
    data.set(val)

def btn0_is_clicked():
    global val
    val = val + "0"
    data.set(val)


#operator functions
def plus_is_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)

def sub_is_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def mul_is_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)

def division_is_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)

def c_is_clicked():
    global A
    global operator
    global val
    A = 0
    val = ""
    operator = ""
    data.set(val)

#result functions
def result():
    global A
    global operator
    global val
    val2 = val
    if operator =="+":
        B = int((val.split("+")[1]))
        C = A+B
        data.set(C)
        val = str(C)
    elif operator =="-":
        B = int((val.split("-")[1]))
        C = A-B
        data.set(C)
        val = str(C)
    elif operator =="*":
        B = int((val.split("*")[1]))
        C = A*B
        data.set(C)
        val = str(C)
    elif operator =="/":
        B = int((val.split("/")[1]))
        if B == 0:
            messagebox.showerror("error","Division by 0 is not supported")
            A = ""
            val = ""
            data.set(val)
        else:
            C = A/B
            data.set(C)
            val = str(C)




root= tkinter.Tk()
root.title("Atik.Calculator")
root.geometry("300x400+250+250")
root.resizable(0,0)

data=StringVar()

#input label
lbl=Label(root, text="0", anchor="se", font=("verdana",20),textvariable=data,background="#fff",fg="#000")
lbl.pack(expand=True, fill="both")

#rows
btnrow1 = Frame(root, )
btnrow1.pack(expand=True, fill="both")

btnrow2 = Frame(root,)
btnrow2.pack(expand=True, fill="both")

btnrow3 = Frame(root, bg="#005500")
btnrow3.pack(expand=True, fill="both")

btnrow4 = Frame(root,)
btnrow4.pack(expand=True, fill="both")

#row1 buttons

btn1 = Button(btnrow1, text="1", font=("verdana",22), relief=GROOVE,border=0,command=btn1_is_clicked,)
btn1.pack(side="left", expand=True, fill="both")
btn2 = Button(btnrow1,text="2", font=("verdana",22),relief=GROOVE,border=0,command=btn2_is_clicked)
btn2.pack(side="left", expand=True, fill="both")
btn3 = Button(btnrow1, text="3", font=("verdana",22),relief=GROOVE,border=0,command=btn3_is_clicked)
btn3.pack(side="left", expand=True, fill="both")
btnplus = Button(btnrow1, text="+", font=("verdana",22),relief=GROOVE,border=0,command=plus_is_clicked)
btnplus.pack(side="left", expand=True, fill="both")

#row2 buttons

btn4 = Button(btnrow2, text="4", font=("verdana",22),relief=GROOVE,border=0,command=btn4_is_clicked)
btn4.pack(side="left", expand=True, fill="both")
btn5 = Button(btnrow2,text="5", font=("verdana",22),relief=GROOVE,border=0,command=btn5_is_clicked)
btn5.pack(side="left", expand=True, fill="both")
btn6 = Button(btnrow2, text="6", font=("verdana",22),relief=GROOVE,border=0,command=btn6_is_clicked)
btn6.pack(side="left", expand=True, fill="both")
btnsub = Button(btnrow2, text="-", font=("verdana",22),relief=GROOVE,border=0,command=sub_is_clicked)
btnsub.pack(side="left", expand=True, fill="both")

#row3 buttons

btn7 = Button(btnrow3, text="7", font=("verdana",22),relief=GROOVE,border=0,command=btn7_is_clicked)
btn7.pack(side="left", expand=True, fill="both")
btn8 = Button(btnrow3,text="8", font=("verdana",22),relief=GROOVE,border=0,command=btn8_is_clicked)
btn8.pack(side="left", expand=True, fill="both")
btn9 = Button(btnrow3, text="9", font=("verdana",22),relief=GROOVE,border=0,command=btn9_is_clicked)
btn9.pack(side="left", expand=True, fill="both")
btn4mul = Button(btnrow3, text="*", font=("verdana",22),relief=GROOVE,border=0,command=mul_is_clicked)
btn4mul.pack(side="left", expand=True, fill="both")

#row4 buttons

btn0 = Button(btnrow4, text="0", font=("verdana",22),relief=GROOVE,border=0,command=btn0_is_clicked)
btn0.pack(side="left", expand=True, fill="both")
btnc = Button(btnrow4, text="C", font=("verdana",22),relief=GROOVE,border=0, command=c_is_clicked)
btnc.pack(side="left", expand=True, fill="both")
btndivision = Button(btnrow4, text="=", font=("verdana",22),relief=GROOVE,border=0,command=result)
btndivision.pack(side="left", expand=True, fill="both")
btnequal = Button(btnrow4,text="/", font=("verdana",22),relief=GROOVE,border=0,command=division_is_clicked)
btnequal.pack(side=LEFT,expand=True, fill="both")




root.mainloop()