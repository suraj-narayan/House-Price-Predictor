import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#loading data
data = pd.read_csv("kc_house_data.csv")
print(data)
x = data.drop(['id','price'],axis=1)
y = data.iloc[:,2]
#preprocessing
x['date'] = [1 if values==2014 else 0 for values in x['date']]

font11 = "-family {Viner Hand ITC} -size 18 -weight bold -slant roman -underline 0 -overstrike 0"

Data1 = {'Sqft': list(data['sqft_lot15']),
         'Price': list(data['price'])
         }

df1 = pd.DataFrame(Data1, columns=['Sqft', 'Price'])

Data2 = {'Floors': list(data['floors']),
         'Price': list(data['price'])
         }

df2 = pd.DataFrame(Data2, columns=['Floors', 'Price'])

Data3 = {'Bedrooms': list(data['bedrooms']),
         'Price': list(data['price'])
         }

df3 = pd.DataFrame(Data3, columns=['Bedrooms', 'Price'])

root = tk.Tk()

Label1 = tk.Label(root, background="#d9d9d9", disabledforeground="#a3a3a3", font=font11, foreground="#000000",
               text="Analyse our data set")

Label1.place(relx=0.163, rely=0.04, height=66, width=562)

figure1 = plt.Figure(figsize=(6, 4), dpi=100)
ax1 = figure1.add_subplot(111)
ax1.scatter(df1['Sqft'], df1['Price'], color='g')
scatter1 = FigureCanvasTkAgg(figure1, root)
scatter1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
ax1.legend()
ax1.set_xlabel('Lot Size(Sqft)')
ax1.set_ylabel('Price')
ax1.set_title('Lot Size vs Price')

figure2 = plt.Figure(figsize=(6, 4), dpi=100)
ax2 = figure2.add_subplot(111)
ax2.scatter(df2['Floors'], df2['Price'], color='g')
scatter2 = FigureCanvasTkAgg(figure2, root)
scatter2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
ax2.legend()
ax2.set_xlabel('Floors')
ax2.set_ylabel('Price')
ax2.set_title('Floors vs Price')

figure3 = plt.Figure(figsize=(6, 4), dpi=100)
ax3 = figure3.add_subplot(111)
ax3.scatter(df3['Bedrooms'], df3['Price'], color='g')
scatter3 = FigureCanvasTkAgg(figure3, root)
scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
ax3.legend()
ax3.set_xlabel('Bedrooms')
ax3.set_ylabel('Price')
ax3.set_title('Bedrooms vs Price')

root.mainloop()