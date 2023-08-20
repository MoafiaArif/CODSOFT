import tkinter
import tkinter.messagebox
from tkinter import *


root = Tk()
root.title("2nd Project To Do List")
root.geometry("650x410+300+150")
root.resizable(False, False)
root.configure(bg="#55ddf2")

task_list=[]
def addTask():
   value = task_entry.get()
   if value:
        listbox.insert(END, value)
        task_entry.delete(0, END)
        save_to_file()
   else: 
        tkinter.messagebox.showwarning(title="Warning!", message= "You must enter a task.")


def load_from_file():
    try:
        with open("tasklist.txt", "r") as file:
            for line in file:
                line = line.strip()
                listbox.insert(END, line)
    except FileNotFoundError:
        pass

def deleteTask():
   selected_index = listbox.curselection()
   if selected_index:
        listbox.delete(selected_index)
        task_entry.delete(0, END)
        save_to_file()
      
   else: 
     tkinter.messagebox.showwarning(title="Warning!", message= "List is empty OR Select an item")


def editTask():
    selected_index = listbox.curselection()
    if selected_index:
        selected_index = selected_index[0]
        new_value = task_entry.get()
        if new_value:
            listbox.delete(selected_index)
            listbox.insert(selected_index, new_value)
            task_entry.delete(0, END)
            save_to_file()
        else:
            tkinter.messagebox.showwarning("Edit Warning", "Please enter a value to edit.")
            
def on_select(event):
    selected_index = listbox.curselection()
    if selected_index:
        selected_index = selected_index[0]
        selected_value = listbox.get(selected_index)
        task_entry.delete(0, END)
        task_entry.insert(0, selected_value)

def save_to_file():
    with open("tasklist.txt", "w") as file:
        for i in range(listbox.size()):
            file.write(listbox.get(i) + "\n")

      


label_preview = Label(root,
                     width=30,
                     height=1,
                     text="To Do List",
                     font=("arial", 30, "bold"),
                     fg="#fff",
                     bg="green")
label_preview.pack()

label_preview = Label(root,
                     width=9,
                     height=1,
                     text="Add Tasks",
                     font=("arial", 24, "bold"),
                     fg="#fff",
                     bg="#268713").place(x=70, y=60)


label_preview = Label(root,
                     width=9,
                     height=1,
                     text="Tasks",
                     font=("arial", 24, "bold"),
                     fg="#fff",
                     bg="#268713").place(x=400, y=60)

frame        = Frame(root,
                     width=300, 
                     height=50,
                     bg="white").place(x=10, y=130)
task=StringVar()
task_entry=Entry(frame,
                 width=16,
                 font=("arial", 24, "bold")
                 )
task_entry.place(x=10, y=130)
task_entry.focus()



button=Button(frame,
       text="Add",
       width=9,
       font=("arial", 24, "bold"),
       bd=3,
       fg="#fff",
       bg="#268713",
       command=addTask).place(x=70, y=200)


frame1        = Frame(root,
                      width=300, 
                     height=250,
                     bg="#c6f7e8").place(x=320, y=130)

listbox=Listbox(frame1,
               font=("arial bold", 12), 
              width=35,
              height=14,
              fg="#07570f", 
              bg="#2ff743",
              cursor="hand2",
              selectbackground="#1d5708" )

listbox.pack( fill=BOTH)
listbox.place(x=320, y=130)



#delete Button
Button(root,
       text="Delete",
       width=9,
       font=("arial", 24, "bold"),
       bd=3,
       fg="#fff",
       bg="#268713",
       command=deleteTask).place(x=70, y=270)


# Edit Button
btn=Button(root,
       text="Edit",
       width=9,
       font=("arial", 24, "bold"),
       bd=3,
       fg="#fff",
       bg="#268713",
       command=editTask).place(x=70, y=340)

listbox.bind('<<ListboxSelect>>', on_select)
load_from_file()

root.mainloop()

