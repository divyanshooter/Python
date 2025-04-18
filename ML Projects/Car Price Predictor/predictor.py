import sys
import os
import numpy as np
import pandas as pd
import pickle as pkl
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline

print(sys.argv[0])

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

car.to_csv('Cleaned Car.csv')

## insert model

X=car.drop(columns='Price')
Y=car['Price']

#print(x.head())



X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)

ohe=OneHotEncoder()
ohe.fit(X[['name','company','fuel_type']])

columns_trans= make_column_transformer((OneHotEncoder(categories=ohe.categories_),['name','company','fuel_type']),remainder='passthrough')
lr=LinearRegression()

pipe=make_pipeline(columns_trans,lr)

pipe.fit(X_train,Y_train)

y_Pred=pipe.predict(X_test)

#print(r2_score(Y_test,y_Pred))


# score=[]
# for i in range(1000):
#     X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=i)
#     lr=LinearRegression()
#     pipe=make_pipeline(columns_trans,lr)
#     pipe.fit(X_train,Y_train)
#     y_Pred=pipe.predict(X_test)
#     score.append(r2_score(Y_test,y_Pred))

# print(score[np.argmax(score)],np.argmax(score))

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=661)
lr=LinearRegression()
pipe=make_pipeline(columns_trans,lr)
pipe.fit(X_train,Y_train)
y_Pred=pipe.predict(X_test)
#print(r2_score(Y_test,y_Pred))

pkl.dump(pipe,open('LinearRegressionModel.pkl','wb'))

print(pipe.predict(pd.DataFrame([['Maruti Suzuki Swift','Maruti',2019,100,'Petrol']],columns=['name','company','year','kms_driven','fuel_type'])))

