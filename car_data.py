# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 18:14:15 2021

@author: Jeremy Chong
"""

#import pandas
import pandas as pd

#insert the name of the OLDER csv in the line below, in the single quotes 
file='june6at1005pmallcars.csv'

#sets up and formats data into the 'old_car_df' dataframe
names =["web-scraper-order", "web-scraper-start-url", "listing links", "stocknumber","mileage","price", "Dealer", "Header", "Dealerindetails", "vin", "Dealership Full Name"]
data = pd.read_csv(file, names = names, delimiter=',')
raw_df = pd.DataFrame(data, columns=names)
old_car_df=raw_df.drop(columns=["Dealerindetails", "web-scraper-order", "listing links", "web-scraper-start-url", "web-scraper-order"])
old_car_df=old_car_df[["vin", "Header", "mileage", "price", "Dealer", "Dealership Full Name", "stocknumber"]]


#insert name of NEWER csv in the line below, in single quotes
file='june13at1135pmallcars.csv'

#sets up dataframe holding newer CSV
data = pd.read_csv(file, names = names, delimiter=',')
raw_df = pd.DataFrame(data, columns=names)
new_car_df=raw_df.drop(columns=["Dealerindetails", "web-scraper-order", "listing links", "web-scraper-start-url", "web-scraper-order"])
new_car_df=new_car_df[["vin", "Header", "mileage", "price", "Dealer", "Dealership Full Name", "stocknumber"]]

#makes empty lists to hold vins
old_vins=[]
new_vins=[]

#reads VINS from both dataframes
for a in old_car_df['vin']:
    old_vins.append(a)
    
for a in new_car_df['vin']:
    new_vins.append(a)

#makes copy of newer vins list in the new_cars list
new_cars=new_vins.copy()

#Checks if each new VIN is in the older list, and removes them from the new cars_list if they're present
for n in new_vins:
    for o in old_vins:
        if n==o:
            new_cars.remove(o)
#makes empty list to hold vins of cars that were sold 
sold_cars=[]

#for each old vin, checks if they appear in the newer vin list. If they aren't, they're added to the list of sold vins.
for o in old_vins:
    if new_vins.count(o)==0:
        sold_cars.append(o)
            
#print (new_cars)
#print (sold_cars)