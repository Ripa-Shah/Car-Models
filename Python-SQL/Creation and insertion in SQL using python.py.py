#!/usr/bin/env python
# coding: utf-8

# In[43]:


import pandas as pd

data = pd.read_csv (r'C:\Users\19498\Downloads\archive(1)\Car_Sales.csv')   
df = pd.DataFrame(data, columns= ['Manufacturer','Model','Sales_in_thousands','year_resale_value','Vehicle_type',
                                  'Price_in_thousands','Engine_size','Horsepower','Wheelbase','Wide','Length','Curb_weight',
                                  'Fuel_capacity','Fuel_efficiency','Latest_Launch','Power_perf_factor'])

print(df)


# In[42]:


import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-M7Q49F6\MSSQL;'
                      'Database=TestDB;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()


# In[44]:


cursor.execute("CREATE TABLE car_info(Manufacturer varchar(100),Model varchar(100),Sales_in_thousands float(20),year_resale_value nvarchar(100),Vehicle_type varchar(100),Price_in_thousands float(20),Engine_size float(10),Horsepower float(10),Wheelbase float(20),Wide float(10),Length float(20),Curb_weight float(20),Fuel_capacity float(20),Fuel_efficiency float(20),Latest_Launch datetime,Power_perf_factor float(20))")
conn.commit()


# In[54]:


for row in df.itertuples():
    cursor.execute('''
                INSERT INTO TestDB.dbo.car_info (Manufacturer,Model,Sales_in_thousands,year_resale_value,Vehicle_type,
                                  Price_in_thousands,Engine_size,Horsepower,Wheelbase,Wide,Length,Curb_weight,
                                  Fuel_capacity,Fuel_efficiency,Latest_Launch,Power_perf_factor)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                ''',
                row.Manufacturer, 
                row.Model,
                row.Sales_in_thousands,
                row.year_resale_value,
                row.Vehicle_type,
                row.Price_in_thousands,
                row.Engine_size,
                row.Horsepower,
                row.Wheelbase,
                row.Wide,
                row.Length,
                row.Curb_weight,
                row.Fuel_capacity,
                row.Fuel_efficiency,
                row.Latest_Launch,
                row.Power_perf_factor
                )
conn.commit()


# In[47]:


col_name =df.columns[9]
df=df.rename(columns = {col_name:'Wide'})
col=df.columns[10]
df=df.rename(columns={col:'Length'})


# In[55]:


conn.commit()


# In[53]:


df = df.fillna(value=0)


# In[ ]:





# In[ ]:





# In[ ]:




