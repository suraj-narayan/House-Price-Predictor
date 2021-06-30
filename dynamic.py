import pandas as pd
from tkinter import *

root3 = Tk()
font12 = "-family SimSun -size 14 -weight bold -slant roman -underline 0 -overstrike 0"
font14 = "-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0"
font9 = "-family {Segoe UI Black} -size 11 -weight bold -slant roman -underline 0 -overstrike 0"
root3.geometry("802x721+596+188")
root3.minsize(148, 1)
root3.maxsize(1924, 1055)
root3.resizable(1, 1)
root3.title("Price Predictor")
root3.configure(background="#d9d9d9")

#loading data
data = pd.read_csv("kc_house_data.csv")
print(data)
x = data.drop(['id','price'],axis=1)
y = data.iloc[:,2]
#preprocessing
x['date'] = [1 if values==2014 else 0 for values in x['date']]
#splitting test train values
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.10, random_state = 2)

year_recorded = IntVar()
year_built = IntVar()
year_renovated = IntVar()
bedrooms = IntVar()
bathrooms = IntVar()
floors = IntVar()
waterfronts = IntVar()
views = IntVar()
condition = IntVar()
grade = IntVar()
total_lot = IntVar()
above = IntVar()
total_living = IntVar()
basement = IntVar()
actual_lot = IntVar()
actual_living = IntVar()
latitude = DoubleVar()
longitude = DoubleVar()
zipcode = IntVar()

year1 = 0
year2 = 0
year3 = 0
bed1 = 0
bath = 0
floors1 = 0
water1 = 0
view1 = 0
cond1 = 0
grade1 = 0
tlot = 0
above1 = 0
tliving = 0
basement1 = 0
alot = 0
aliving = 0
lat = 0
lon = 0
zipcode1 = 0

def submit():
    global year_recorded,year_built,year_renovated,zipcode,bedrooms,bathrooms,floors,waterfronts,views,condition,grade,total_lot,above,total_living,basement,actual_living,actual_lot,latitude,longitude
    global year1,year2,year3,bed1,bath,floors1,water1,view1,cond1,grade1,tlot,above1,tlving,basement1,alot,aliving,lat,lon,zipcode1
    year1=year_recorded.get()
    year1 = 0 if year1<=2014 else 1
    year2=year_built.get()
    year3=year_renovated.get()
    bed1=bedrooms.get()
    bath=bathrooms.get()
    floors1=floors.get()
    water1=waterfronts.get()
    view1=views.get()
    cond1=condition.get()
    grade1=grade.get()
    tlot=total_lot.get()
    above1=above.get()
    tliving=total_living.get()
    basement1=basement.get()
    alot=actual_lot.get()
    aliving=actual_living.get()
    lat=latitude.get()
    lon=longitude.get()
    zipcode1=zipcode.get()
    print("Data Fetched: ",year1,year2,year3,bed1,bath,floors1,water1,view1,cond1,grade1,tlot,above1,basement1,alot,aliving,tliving,lat,lon,zipcode1)

    # training the model
    from sklearn import ensemble
    clf = ensemble.GradientBoostingRegressor(n_estimators=400, max_depth=5, min_samples_split=2, learning_rate=0.1, loss="ls")
    clf.fit(x_train, y_train)
    col = list(x_test.columns.values)
    x_d_data = [[year1,bed1, bath, aliving, alot, floors1, water1, view1, cond1, grade1, above1, basement1, year2, year3, zipcode1, lat, lon, tliving, tlot]]
    x_d = pd.DataFrame(x_d_data,columns=col)
    print(x_d)
    y = clf.predict(x_d)
    print(y)
    Labelpred.configure(text=y[0])

tlabel = Label(root3)
tlabel.place(relx=0.187, rely=0.0, height=80, width=504)
tlabel.configure(background="#d9d9d9")
tlabel.configure(font="-family {ROG Fonts} -size 26 -weight bold -slant roman -underline 0 -overstrike 0")
tlabel.configure(text='''Price Predictor''')

Labelframe1 = LabelFrame(root3)
Labelframe1.place(relx=0.087, rely=0.139, relheight=0.229, relwidth=0.374)
Labelframe1.configure(relief='groove')
Labelframe1.configure(font=font12)
Labelframe1.configure(text='''Year details''')
Labelframe1.configure(background="#d9d9d9")

label31 = Label(Labelframe1)
label31.place(relx=0.067, rely=0.182, height=41, width=145, bordermode='ignore')
label31.configure(background="#d9d9d9")
label31.configure(font=font9)
label31.configure(text='''Year Recorded''')

label32 = Label(Labelframe1)
label32.place(relx=0.2, rely=0.424, height=41, width=104, bordermode='ignore')
label32.configure(background="#d9d9d9")
label32.configure(font=font9)
label32.configure(text='''Year Built''')

Entry1 = Entry(Labelframe1,textvar=year_built)
Entry1.place(relx=0.6, rely=0.485, height=24, relwidth=0.313, bordermode='ignore')
Entry1.configure(font="TkFixedFont")

Label3 = Label(Labelframe1)
Label3.place(relx=0.033, rely=0.667, height=41, width=156, bordermode='ignore')
Label3.configure(background="#d9d9d9")
Label3.configure(font=font9)
Label3.configure(text='''Year Renovated''')

Entry1_1 = Entry(Labelframe1,textvar=year_renovated)
Entry1_1.place(relx=0.6, rely=0.727, height=24, relwidth=0.313, bordermode='ignore')
Entry1_1.configure(font="TkFixedFont")

Entry1_2 = Entry(Labelframe1,textvar=year_recorded)
Entry1_2.place(relx=0.6, rely=0.242, height=24, relwidth=0.313, bordermode='ignore')
Entry1_2.configure(font="TkFixedFont")


Labelframe2 = LabelFrame(root3)
Labelframe2.place(relx=0.087, rely=0.388, relheight=0.451, relwidth=0.374)
Labelframe2.configure(relief='groove')
Labelframe2.configure(font=font12)
Labelframe2.configure(text='''Amneties''')
Labelframe2.configure(background="#d9d9d9")

Label4 = Label(Labelframe2)
Label4.place(relx=0.2, rely=0.092, height=41, width=106, bordermode='ignore')
Label4.configure(background="#d9d9d9")
Label4.configure(font=font9)
Label4.configure(text='''Bedrooms''')

Spinbox1 = Spinbox(Labelframe2, from_=1.0, to=100.0)
Spinbox1.place(relx=0.6, rely=0.123, relheight=0.074, relwidth=0.153, bordermode='ignore')
Spinbox1.configure(textvariable=bedrooms)

Spinbox1_6 = Spinbox(Labelframe2, from_=1.0, to=100.0)
Spinbox1_6.place(relx=0.6, rely=0.246, relheight=0.074, relwidth=0.153, bordermode='ignore')
Spinbox1_6.configure(textvariable=bathrooms)

Label4_7 = Label(Labelframe2)
Label4_7.place(relx=0.167, rely=0.215, height=41, width=116, bordermode='ignore')
Label4_7.configure(background="#d9d9d9")
Label4_7.configure(font=font9)
Label4_7.configure(text='''Bathrooms''')

Spinbox1_7 = Spinbox(Labelframe2, from_=1.0, to=100.0)
Spinbox1_7.place(relx=0.6, rely=0.369, relheight=0.074, relwidth=0.153, bordermode='ignore')
Spinbox1_7.configure(textvariable=floors)

Label4_8 = Label(Labelframe2)
Label4_8.place(relx=0.3, rely=0.338, height=41, width=76, bordermode='ignore')
Label4_8.configure(background="#d9d9d9")
Label4_8.configure(font=font9)
Label4_8.configure(text='''Floors''')

Label4_9 = Label(Labelframe2)
Label4_9.place(relx=0.133, rely=0.462, height=41, width=126, bordermode='ignore')
Label4_9.configure(background="#d9d9d9")
Label4_9.configure(font=font9)
Label4_9.configure(text='''Waterfronts''')

Spinbox1_8 = Spinbox(Labelframe2, from_=1.0, to=100.0)
Spinbox1_8.place(relx=0.6, rely=0.492, relheight=0.074, relwidth=0.153, bordermode='ignore')
Spinbox1_8.configure(textvariable=waterfronts)

Label4_10 = Label(Labelframe2)
Label4_10.place(relx=0.333, rely=0.585, height=41, width=66, bordermode='ignore')
Label4_10.configure(background="#d9d9d9")
Label4_10.configure(font=font9)
Label4_10.configure(text='''Views''')

Spinbox1_9 = Spinbox(Labelframe2, from_=1.0, to=100.0)
Spinbox1_9.place(relx=0.6, rely=0.615, relheight=0.074, relwidth=0.153, bordermode='ignore')
Spinbox1_9.configure(textvariable=views)

Label4_11 = Label(Labelframe2)
Label4_11.place(relx=0.2, rely=0.708, height=41, width=116, bordermode='ignore')
Label4_11.configure(background="#d9d9d9")
Label4_11.configure(font=font9)
Label4_11.configure(text='''Condition''')

Spinbox1_10 = Spinbox(Labelframe2, from_=1.0, to=5.0)
Spinbox1_10.place(relx=0.6, rely=0.738, relheight=0.074, relwidth=0.153, bordermode='ignore')
Spinbox1_10.configure(textvariable=condition)

Spinbox1_10 = Spinbox(Labelframe2, from_=1.0, to=15.0)
Spinbox1_10.place(relx=0.6, rely=0.862, relheight=0.074, relwidth=0.153, bordermode='ignore')
Spinbox1_10.configure(textvariable=grade)

Label4_12 = Label(Labelframe2)
Label4_12.place(relx=0.333, rely=0.831, height=41, width=76, bordermode='ignore')
Label4_12.configure(background="#d9d9d9")
Label4_12.configure(font=font9)
Label4_12.configure(text='''Grade''')

Labelframe3 = LabelFrame(root3)
Labelframe3.place(relx=0.524, rely=0.139, relheight=0.395, relwidth=0.399)
Labelframe3.configure(relief='groove')
Labelframe3.configure(font=font12)
Labelframe3.configure(text='''Area(In Sqft)''')
Labelframe3.configure(background="#d9d9d9")

Label5 = Label(Labelframe3)
Label5.place(relx=0.094, rely=0.105, height=46, width=105, bordermode='ignore')
Label5.configure(background="#d9d9d9")
Label5.configure(font=font9)
Label5.configure(text='''Total Lot''')

Entry2 = Entry(Labelframe3,textvar=total_lot)
Entry2.place(relx=0.469, rely=0.14, height=24, relwidth=0.356, bordermode='ignore')
Entry2.configure(font="TkFixedFont")

Entry2_13 = Entry(Labelframe3,textvar=above)
Entry2_13.place(relx=0.469, rely=0.281, height=24, relwidth=0.356, bordermode='ignore')
Entry2_13.configure(font="TkFixedFont")

Label5_14 = Label(Labelframe3)
Label5_14.place(relx=0.156, rely=0.246, height=46, width=85, bordermode='ignore')
Label5_14.configure(background="#d9d9d9")
Label5_14.configure(font=font9)
Label5_14.configure(text='''Above''')

Label5_15 = Label(Labelframe3)
Label5_15.place(relx=0.031, rely=0.386, height=46, width=115, bordermode='ignore')
Label5_15.configure(background="#d9d9d9")
Label5_15.configure(font=font9)
Label5_15.configure(text='''Total Living''')

Entry2_14 = Entry(Labelframe3,textvar=total_living)
Entry2_14.place(relx=0.469, rely=0.421, height=24, relwidth=0.356, bordermode='ignore')
Entry2_14.configure(font="TkFixedFont")

Label5_16 = Label(Labelframe3)
Label5_16.place(relx=0.063, rely=0.526, height=46, width=125, bordermode='ignore')
Label5_16.configure(background="#d9d9d9")
Label5_16.configure(font=font9)
Label5_16.configure(text='''Basement''')

Entry2_15 =Entry(Labelframe3,textvar=basement)
Entry2_15.place(relx=0.469, rely=0.561, height=24, relwidth=0.356, bordermode='ignore')
Entry2_15.configure(font="TkFixedFont")

Label5_16 = Label(Labelframe3)
Label5_16.place(relx=0.094, rely=0.667, height=46, width=105, bordermode='ignore')
Label5_16.configure(background="#d9d9d9")
Label5_16.configure(font=font9)
Label5_16.configure(text='''Actual Lot''')

Label5_16 = Label(Labelframe3)
Label5_16.place(relx=0.031, rely=0.807, height=46, width=125, bordermode='ignore')
Label5_16.configure(background="#d9d9d9")
Label5_16.configure(font=font9)
Label5_16.configure(text='''Actual Living''')

Entry2_16 = Entry(Labelframe3,textvar=actual_lot)
Entry2_16.place(relx=0.469, rely=0.702, height=24, relwidth=0.356, bordermode='ignore')
Entry2_16.configure(font="TkFixedFont")

Entry2_16 = Entry(Labelframe3,textvar=actual_living)
Entry2_16.place(relx=0.469, rely=0.842, height=24, relwidth=0.356, bordermode='ignore')
Entry2_16.configure(font="TkFixedFont")

Labelframe4 = LabelFrame(root3)
Labelframe4.place(relx=0.524, rely=0.569, relheight=0.27, relwidth=0.387)
Labelframe4.configure(relief='groove')
Labelframe4.configure(font=font12)
Labelframe4.configure(text='''Location''')
Labelframe4.configure(background="#d9d9d9")

Label6 = Label(Labelframe4)
Label6.place(relx=0.129, rely=0.205, height=41, width=101, bordermode='ignore')
Label6.configure(background="#d9d9d9")
Label6.configure(font=font9)
Label6.configure(text='''Latitude''')

Scale1 = Scale(Labelframe4, from_=47.156, to=47.778, variable=latitude)
Scale1.place(relx=0.484, rely=0.154, relwidth=0.342, relheight=0.0, height=47, bordermode='ignore')
Scale1.configure(activebackground="#ececec")
Scale1.configure(background="#d9d9d9")
Scale1.configure(font=font14)
Scale1.configure(foreground="#000000")
Scale1.configure(highlightbackground="#d9d9d9")
Scale1.configure(highlightcolor="black")
Scale1.configure(orient="horizontal")
Scale1.configure(resolution="0.001")
Scale1.configure(troughcolor="#d9d9d9")

Label6_17 = Label(Labelframe4)
Label6_17.place(relx=0.097, rely=0.462, height=41, width=101, bordermode='ignore')
Label6_17.configure(background="#d9d9d9")
Label6_17.configure(font=font9)
Label6_17.configure(text='''Longitude''')

Scale1_18 = Scale(Labelframe4, from_=-122.519, to=-121.315, variable=longitude)
Scale1_18.place(relx=0.484, rely=0.41, relwidth=0.342, relheight=0.0, height=47, bordermode='ignore')
Scale1_18.configure(activebackground="#ececec")
Scale1_18.configure(background="#d9d9d9")
Scale1_18.configure(font="-family {Segoe UI} -size 9 -weight bold")
Scale1_18.configure(foreground="#000000")
Scale1_18.configure(highlightbackground="#d9d9d9")
Scale1_18.configure(highlightcolor="black")
Scale1_18.configure(orient="horizontal")
Scale1_18.configure(resolution="0.001")
Scale1_18.configure(troughcolor="#d9d9d9")

Label6_18 = Label(Labelframe4)
Label6_18.place(relx=0.129, rely=0.718, height=41, width=101, bordermode='ignore')
Label6_18.configure(background="#d9d9d9")
Label6_18.configure(font="-family {Segoe UI Black} -size 11 -weight bold")
Label6_18.configure(foreground="#000000")
Label6_18.configure(text='''Zipcode''')

Entry3 = Entry(Labelframe4,textvar=zipcode)
Entry3.place(relx=0.484, rely=0.769, height=24, relwidth=0.320, bordermode='ignore')
Entry3.configure(font="TkFixedFont")

Button1 = Button(root3,command=submit)
Button1.place(relx=0.826, rely=0.874, height=70, width=70)
Button1.configure(background="#d9d9d9")
predict_img = PhotoImage(file="verified.png")
Button1.configure(image=predict_img)
Button1.configure(pady="0")

Labelpred = Label(root3)
Labelpred.place(relx=0.05, rely=0.894, height=41, width=500, bordermode='ignore')
Labelpred.configure(background="#d9d9d9")
Labelpred.configure(font="-family {Segoe UI Black} -size 16 -weight bold")
Labelpred.configure(foreground="#000000")
Labelpred.configure(text="Predicted price will appear here..")

root3.mainloop()
