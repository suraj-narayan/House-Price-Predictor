
import pandas as pd
import os
import matplotlib.pyplot as plt
from tkinter import *
import tkinter.ttk as ttk
data=pd.DataFrame(data=None)
x_train=pd.DataFrame(data=None)
x_test=pd.DataFrame(data=None)
y_train=pd.DataFrame(data=None)
y_test=pd.DataFrame(data=None)
y_pred=pd.DataFrame(data=None)

def sel_data():
#if var1 == 1:
    global data,x_train, x_test, y_train, y_test
    data = pd.read_csv("kc_house_data.csv")
    print(data)
    x = data.drop(['id','price'],axis=1)
    y = data.iloc[:,2]
    #preprocessing
    x['date'] = [1 if values==2014 else 0 for values in x['date']]
    #splitting test train values
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.10, random_state = 2)
#else:
  #  label1.configure(text = "You have to click on atleast one option from above!")

def algomodule():
    # implementing linear regression
    def nextfunc():
        os.system("analyse.py")
    def linear():
        print("Implementing Linear Regression")
        from sklearn.linear_model import LinearRegression
        regressor = LinearRegression()
        regressor.fit(x_train, y_train)
        scorestr = str(int(regressor.score(x_test,y_test)*100)) + "% Accurate"
        print(regressor.score(x_test, y_test))
        Labelscore.configure(text=scorestr)

    def grad():
        print("Implementing Gradient Boosting")
        from sklearn import ensemble
        clf = ensemble.GradientBoostingRegressor(n_estimators=400, max_depth=5, min_samples_split=2, learning_rate=0.1,
                                                 loss="ls")
        clf.fit(x_train, y_train)
        scorestr = str(int(clf.score(x_test, y_test) * 100)) + "% Accurate"
        print(clf.score(x_test, y_test))
        Labelscore.configure(text=scorestr)
    root2 = Toplevel()
    font11 = "-family {Viner Hand ITC} -size 18 -weight bold -slant roman -underline 0 -overstrike 0"
    font13 = "-family {Tempus Sans ITC} -size 14 -weight bold -slant roman -underline 0 -overstrike 0"
    font14 = "-family {Tempus Sans ITC} -size 12 -weight bold -slant roman -underline 0 -overstrike 0"
    font12 = "-family {Tempus Sans ITC} -size 14 -weight bold -slant roman -underline 0 -overstrike 0"
    root2.geometry("800x500")
    root2.title("Algorithm Selection")
    root2.configure(background="#d9d9d9")

    Label1 = Label(root2,background="#d9d9d9",disabledforeground="#a3a3a3",font=font11,foreground="#000000",text="Which algorithm do you want to use?")
    Label1.place(relx=0.163, rely=0.04, height=66, width=562)

    TSeparator3 = ttk.Separator(root2)
    TSeparator3.place(relx=0.075, rely=0.2, relwidth=0.875)

    gbimg=PhotoImage(file=r"decision-tree.png")
    mrimg=PhotoImage(file=r"mr.png")
    option1 = Radiobutton(root2,cursor="hand2",image=gbimg,justify='left',indicatoron = 0,command=grad)
    option1.place(relx=0.163, rely=0.29, relheight=0.36, relwidth = 0.296)

    option2 = Radiobutton(root2,indicatoron = 0,image=mrimg,command=linear)
    option2.place(relx=0.593, rely=0.28, relheight=0.402, relwidth = 0.251)
    option2.configure(activebackground="#ececec")
    option2.configure(activeforeground="#000000")
    option2.configure(background="#d9d9d9")
    option2.configure(cursor="hand2")
    option2.configure(disabledforeground="#a3a3a3")
    option2.configure(foreground="#000000")
    option2.configure(highlightbackground="#d9d9d9")
    option2.configure(highlightcolor="black")

    Gblabel = Label(root2)
    Gblabel.place(relx=0.1, rely=0.68, height=42, width=332)
    Gblabel.configure(background="#d9d9d9")
    Gblabel.configure(disabledforeground="#a3a3a3")
    Gblabel.configure(font=font14)
    Gblabel.configure(foreground="#000000")
    Gblabel.configure(text='''Gradient Boosting (more accurate)''')

    Mrlabel = Label(root2)
    Mrlabel.place(relx=0.6, rely=0.68, height=36, width=192)
    Mrlabel.configure(background="#d9d9d9")
    Mrlabel.configure(disabledforeground="#a3a3a3")
    Mrlabel.configure(font=font12)
    Mrlabel.configure(foreground="#000000")
    Mrlabel.configure(text='''Linear Regression''')

    nextimg = PhotoImage(file=r"next.png")
    nextbutton = Button(root2,cursor="hand2",image=nextimg,command=nextfunc)
    nextbutton.place(relx=0.875, rely=0.84, height=70, width=70)
    nextbutton.configure(pady="0")

    Labelscore = Label(root2)
    Labelscore.place(relx=0.09, rely=0.845, height=41, width=500, bordermode='ignore')
    Labelscore.configure(background="#d9d9d9")
    Labelscore.configure(font="-family {Segoe UI Black} -size 16 -weight bold")
    Labelscore.configure(foreground="#000000")
    Labelscore.configure(text="Selected Algorithm's accuracy will be shown..")

    root2.mainloop()

#selecting data set
root1 = Tk()

root1.configure(background="#ebbe63")
#menubar
menubar = Menu(root1)
root1.config(menu=menubar)
root1.title("Data Set Selection")
root1.geometry("800x500")
#data set heading
font12 = "-family {Snap ITC} -size 18 -weight normal -slant roman -underline 1 -overstrike 0"
Label1 = Label(root1)
Label1.place(relx=0.430, rely=0.019, height=46, width=145)
Label1.configure(background="#ebbe63")
Label1.configure(disabledforeground="#a3a3a3")
Label1.configure(font=font12)
Label1.configure(foreground="#2957a3")
Label1.configure(text='''Data-Set''')
#hl
TSeparator1 = ttk.Separator(root1)
TSeparator1.place(relx=0.038, rely=0.131, relwidth=0.945)
TSeparator1.configure(takefocus="0")

TSeparator2 = ttk.Separator(root1)
TSeparator2.place(relx=0.529, rely=0.205, relheight=0.709)
TSeparator2.configure(orient="vertical")
TSeparator2.configure(takefocus="0")

#dataset options
v1 = IntVar()
rdata1 = Radiobutton(root1,activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",variable=v1,value=1,command=sel_data)
rdata1.place(relx=0.106, rely=0.305, relheight=0.069, relwidth=0.285)
font10 = "-family {Segoe UI Black} -size 11 -weight bold -slant roman -underline 0 -overstrike 0"
rdata1.configure(font=font10)
rdata1.configure(foreground="#3d8d96")
rdata1.configure(highlightbackground="#d9d9d9")
rdata1.configure(highlightcolor="black")
rdata1.configure(justify='left')
rdata1.configure(offrelief="ridge")
rdata1.configure(relief="ridge")
rdata1.configure(takefocus="0")
rdata1.configure(text='''King Country,Washington''')

#continue
photo = PhotoImage(file = r"buttoncontinue.png")
nextbutton = Button(root1, image=photo,command=algomodule)
nextbutton.place(relx=0.610, rely=0.448)

#label
font12 = "-family {Segoe UI Black} -size 11 -weight bold -slant roman -underline 0 -overstrike 0"
Label2 = Label(root1,cursor="sb_up_arrow",background="#ebbe63",disabledforeground="#a3a3a3",foreground="#5882ab",text="Please select a dataset from above")
Label2.place(relx=0.076, rely=0.728, height=56, width=332)
Label2.configure(font=font12)

Label3 = Label(root1,cursor="sb_up_arrow")
Label3.place(relx=0.567, rely=0.746, height=36, width=322)
Label3.configure(background="#ebbe63")
Label3.configure(disabledforeground="#a3a3a3")
Label3.configure(font=font12)
Label3.configure(foreground="#5882ab")
Label3.configure(text="Click on above button to proceed")

root1.mainloop()
