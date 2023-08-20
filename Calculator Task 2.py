import tkinter
from tkinter import *
import math

root = Tk()
root.title("1st Project Calculator")
root.geometry("550x700+100+200")
root.resizable(False, False)
root.configure(bg="#55ddf2")
equation = ""

def show(answer):
    global equation
    equation += answer
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            if '!' in equation:
                num = int(equation[:-1])
                result = math.factorial(num)
            elif '√' in equation:
                num = float(equation[1:])
                result = math.sqrt(num)
            else:
                result = eval(equation)
        except:
            result = "error"
        equation = str(result)
    label_result.config(text=result)


label_result = Label(root,
                     width=25,
                     height=2,
                     text="",
                     font=("TimeNewRoman", 30),
                     bg="#ebb9b9")
label_result.pack()


  
Button(root,
       text="C",
       width=4,
       height=1,
       font=("arial", 30, "bold"),
       bd=1,
       fg="#fff",
       bg="#eda832",
       command=lambda: clear()).place(x=10, y=100)
Button(root,
       text="/",
       width=4,
       height=1,
       font=("arial", 30, "bold"),
       bd=1,
       fg="#fff",
       bg="#1c4dd4",
       command=lambda: show("/")).place(x=150, y=100)
Button(root,
       text="%",
       width=4,
       height=1,
       font=("arial", 30, "bold"),
       bd=1,
       fg="#fff",
       bg="#1c4dd4",
       command=lambda: show("%")).place(x=290, y=100)
Button(root,
       text="*",
       width=4,
       height=1,
       font=("arial", 30, "bold"),
       bd=1,
       fg="#fff",
       bg="#1c4dd4",
       command=lambda: show("*")).place(x=430, y=100)

Button(root,
       text="!",
       width=4,
       height=1,
       font=("arial", 30, "bold"),
       bd=1,
       fg="#fff",
       bg="#1c4dd4",
       command=lambda: show("!")).place(x=10, y=200)

Button(root,
       text="(",
       width=4,
       height=1,
       font=("arial", 30, "bold"),
       bd=1,
       fg="#fff",
       bg="#1c4dd4",
       command=lambda: show("(")).place(x=150, y=200)

Button(root,
       text=")",
       width=4,
       height=1,
       font=("arial", 30, "bold"),
       bd=1,
       fg="#fff",
       bg="#1c4dd4",
       command=lambda: show(")")).place(x=290, y=200)

Button(root,
       text="7",
       width=4,
       height=1,
       font=("arial", 30, "bold"),
       bd=1,
       fg="#fff",
       bg="#b832ed",
       command=lambda: show("7")).place(x=10, y=300)
Button(root,
       text="8",
       width=4,
       height=1,
       font=("arial", 30, "bold"),
       bd=1,
       fg="#fff",
       bg="#b832ed",
       command=lambda: show("8")).place(x=150, y=300)
Button(root,
       text="9",
       width=4,
       height=1,
       font=("arial", 30, "bold"),
       bd=1,
       fg="#fff",
       bg="#b832ed",
       command=lambda: show("9")).place(x=290, y=300)
Button(root,
       text="-",
       width=4,
       height=1,
       font=("arial", 30, "bold"),
       bd=1,
       fg="#fff",
       bg="#1c4dd4",
       command=lambda: show("-")).place(x=430, y=300)

Button(root,
       text="4",
       width=4,
       height=1,
       font=("arial", 30, "bold"),
       bd=1,
       fg="#fff",
       bg="#b832ed",
       command=lambda: show("4")).place(x=10, y=400)
Button(root,
       text="5",
       width=4,
       height=1,
       font=("arial", 30, "bold"),
       bd=1,
       fg="#fff",
       bg="#b832ed",
       command=lambda: show("5")).place(x=150, y=400)
Button(root,
       text="6",
       width=4,
       height=1,
       font=("arial", 30, "bold"),
       bd=1,
       fg="#fff",
       bg="#b832ed",
       command=lambda: show("6")).place(x=290, y=400)
Button(root,
       text="+",
       width=4,
       height=1,
       font=("arial", 30, "bold"),
       bd=1,
       fg="#fff",
       bg="#1c4dd4",
       command=lambda: show("+")).place(x=430, y=200)

Button(root,
       text="1",
       width=4,
       height=1,
       font=("arial", 30, "bold"),
       bd=1,
       fg="#fff",
       bg="#b832ed",
       command=lambda: show("1")).place(x=10, y=500)
Button(root,
       text="2",
       width=4,
       height=1,
       font=("arial", 30, "bold"),
       bd=1,
       fg="#fff",
       bg="#b832ed",
       command=lambda: show("2")).place(x=150, y=500)
Button(root,
       text="3",
       width=4,
       height=1,
       font=("arial", 30, "bold"),
       bd=1,
       fg="#fff",
       bg="#b832ed",
       command=lambda: show("3")).place(x=290, y=500)

 
Button(root,
       text="√x",
       width=4,
       height=1,
       font=("arial", 30, "bold"),
       bd=1,
       fg="#fff",
       bg="#1c4dd4",
        command=lambda: show("√")).place(x=430, y=400)

Button(root,
       text="0",
       width=11,
       height=1,
       font=("arial", 30, "bold"),
       bd=1,
       fg="#fff",
       bg="#1c4dd4",
       command=lambda: show("0")).place(x=10, y=600)

Button(root,
       text=".",
       width=4,
       height=1,
       font=("arial", 30, "bold"),
       bd=1,
       fg="#fff",
       bg="#1c4dd4",
       command=lambda: show(".")).place(x=290, y=600)

Button(root,
       text="=",
       width=4,
       height=3,
       font=("arial", 30, "bold"),
       bd=1,
       fg="#fff",
       bg="#d41c3a",
       command=lambda: calculate()).place(x=430, y=500)

root.mainloop()
