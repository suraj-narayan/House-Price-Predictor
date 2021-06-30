from tkinter import *

top=Tk()
_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#d9d9d9'  # X11 color: 'gray85'
_ana1color = '#d9d9d9'  # X11 color: 'gray85'
_ana2color = '#ececec'  # Closest X11 color: 'gray92'
font10 = "-family {Segoe UI} -size 30 -weight normal -slant roman -underline 1 -overstrike 0"

top.geometry("600x450+263+391")
top.minsize(148, 1)
top.maxsize(1924, 1055)
top.resizable(1, 1)
top.title("Help")
top.configure(background="#d9d9d9")

Label1 = Label(top)
Label1.place(relx=0.333, rely=0.022, height=66, width=202)
Label1.configure(background="#d9d9d9")
Label1.configure(disabledforeground="#a3a3a3")
Label1.configure(foreground="#000000")
Label1.configure(font=font10)
Label1.configure(text='''Help?''')

Label2 = Label(top)
Label2.place(relx=-0.033, rely=0.2, height=36, width=462)
Label2.configure(background="#d9d9d9")
Label2.configure(text='''●Press "Test Algorithm"-->"King city,washington"-->continue''')

Label3 = Label(top)
Label3.place(relx=0.033, rely=0.25, height=16, width=272)
Label3.configure(background="#d9d9d9")
Label3.configure(text='''to check the accuracy of the algorithm''')

Label4 = Label(top)
Label4.place(relx=0.0, rely=0.289, height=26, width=402)
Label4.configure(background="#d9d9d9")
Label4.configure(text='''●Press "predictor" to give your inputs and predict the price''')

Label5 = Label(top)
Label5.place(relx=0.0, rely=0.33, height=16, width=432)
Label5.configure(background="#d9d9d9")
Label5.configure(text='''Enter all the columns manually,all the columns are compulsory''')

Label6 = Label(top)
Label6.place(relx=0.054, rely=0.36, height=16, width=156)
Label6.configure(background="#d9d9d9")
Label6.configure(text='''for maximum accuracy''')

Label7 = Label(top)
Label7.place(relx=0.0, rely=0.444, height=26, width=331)
Label7.configure(background="#d9d9d9")
Label7.configure(text='''●For more queries mail to psrealtors@gmail.com''')

top.mainloop()