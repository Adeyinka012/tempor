from tkinter import *
from datetime import date 
root= Tk()
root.title("setting up tkinter")
root.geometry('400x300')
lbl=Label(text="Hey there!! ", fg='#42b9f5', bg="#15409b",height=1,width=300)
name_lbl=Label(text="Full name", bg="#42b9f5",)
name_entry=Entry()
def display():
    name=name_entry.get()
    global Message
    message="welcome to the application! \n Today's date is:"
    greet="Hello ", name, "\n"
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today)
text_box=Text(height=4)
btn=Button(text="Begin", command=display, height=1,bg="#42b9f5", fg="#639cb8")
lbl.pack()
name_lbl.pack()
btn.pack()
text_box.pack()
root.mainloop()


