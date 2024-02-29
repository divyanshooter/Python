import pandas as pd

car=pd.read_csv('./Dataset/quikr_car.csv')
"""print(car.head())

print(car.shape)
print(car.info())
print(car['year'].unique())

print(car['Price'].unique())
print(car['Price'].dtype)"""

car_bkp=car.copy()

# year cleaning
car=car[car['year'].str.isnumeric()]
car['year']=car['year'].astype('int32')
#print(car.info())

#price cleaning
car=car[car['Price']!='Ask For Price']
car['Price']=car['Price'].str.replace(',','').astype('int32')
#print(car.info())

#kms_driven cleaning
car['kms_driven']=car['kms_driven'].str.split(' ').str.get(0).str.replace(',','')
car=car[car['kms_driven'].str.isnumeric()]
car['kms_driven']=car['kms_driven'].astype('int')
#print(car.info())

#fuel_type cleaning
car=car[~car['fuel_type'].isnull()]
#print(car.info())

#name cleaning
car['name']=car['name'].str.split(' ').str.slice(0,3).str.join(' ')
car.reset_index(inplace=True,drop=True)
#print(car.describe())

#removing outlier
car=car[car['Price']<6e6].reset_index(drop=True)
#print(car.shape)

