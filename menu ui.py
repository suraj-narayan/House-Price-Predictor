from tkinter import *
import os
def execdynamic():
    top.destroy()
    os.system("dynamic.py")
def execproject():
    top.destroy()
    os.system("Project.py")
def exechelp():
    top.destroy()
    os.system("help.py")
top = Tk()
font14 = "-family {Segoe UI} -size 13 -weight normal -slant roman -underline 0 -overstrike 0"
font15 = "-family {Segoe UI} -size 14 -weight normal -slant roman -underline 0 -overstrike 0"
font18 = "-family {Segoe UI} -size 30 -weight bold -slant roman -underline 0 -overstrike 0"
font19 = "-family Constantia -size 22 -weight bold -slant roman -underline 1 -overstrike 0"

top.geometry("600x450+650+150")
top.minsize(148, 1)
top.maxsize(1924, 1055)
top.resizable(1, 1)
top.title("Main Menu")
top.configure(background="#ba5536")

Label1 = Label(top)
Label1.place(relx=0.333, rely=0.244, height=86, width=212)
Label1.configure(background="#ba5536")
Label1.configure(font=font19)
Label1.configure(justify='right')
Label1.configure(text='''MENU''')

Button1 = Button(top,command=execproject)
Button1.place(relx=0.35, rely=0.444, height=53, width=200)
Button1.configure(activebackground="#ececec")
Button1.configure(activeforeground="#000000")
Button1.configure(background="#a43820")
Button1.configure(cursor="hand2")
Button1.configure(disabledforeground="#a3a3a3")
Button1.configure(font=font14)
Button1.configure(foreground="#000000")
Button1.configure(highlightbackground="#d9d9d9")
Button1.configure(highlightcolor="black")
Button1.configure(overrelief="raised")
Button1.configure(pady="5")
Button1.configure(text='''Test Algorithm''')

Button3 = Button(top,command=execdynamic)
Button3.place(relx=0.35, rely=0.622, height=53, width=196)
Button3.configure(activebackground="#ececec")
Button3.configure(activeforeground="#000000")
Button3.configure(background="#ff0000")
Button3.configure(cursor="hand2")
Button3.configure(disabledforeground="#a3a3a3")
Button3.configure(font=font15)
Button3.configure(foreground="#000000")
Button3.configure(highlightbackground="#d9d9d9")
Button3.configure(highlightcolor="black")
Button3.configure(pady="0")
Button3.configure(text='''Predictor''')

TButton1 = Button(top,command=exechelp)
TButton1.place(relx=0.817, rely=0.889, height=30, width=98)
TButton1.configure(takefocus="")
TButton1.configure(text='''Help?��''')
TButton1.configure(cursor="question_arrow")


Label2 = Label(top)
Label2.place(relx=0.117, rely=0.067, height=56, width=472)
Label2.configure(activebackground="#ba5536")
Label2.configure(activeforeground="white")
Label2.configure(background="#ba5536")
Label2.configure(disabledforeground="#a3a3a3")
Label2.configure(font=font18)
Label2.configure(foreground="#152b4a")
Label2.configure(text='''House-Price Predictor''')
top.mainloop()