from numerical_data.nse_stocks.pfizer import PFIZER
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn import preprocessing
# load the iris dataset
import pandas as pd

# from numerical_data.nse_stocks.sunpharma import SUNPHARMA
# from numerical_data.nse_stocks.pfizer import PFIZER
# from numerical_data.exchanges.sensex import SENSEX
# from numerical_data.exchanges.nifty50 import NIFTY


pfizer = PFIZER()

# pfizer.technical_indicators()
df_ti = pfizer.retrieve_ti()
df = pfizer.retrieve_inter_day_data()
# print(df_ti.columns)
y = df["Close"]
y = y.iloc[90:]
# print(df_ti)
date = df_ti['Date']
df_ti.drop(columns=['_id', 'RSI_6', 'RSI_12'], axis=1, inplace=True)
# print(df_ti)

df.drop(columns=['Date','_id','Low','Close'], axis=1, inplace=True)
frames = [df,df_ti]
X = pd.concat(frames,axis=1,sort=False)

X = X.iloc[90:]
# print(X.head())

X["Volume"] = X["Volume"]*0.7
X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.25,shuffle=False)
X_train = X_train.drop(columns=['Date'])
date = pd.to_datetime(X_test['Date'])
X_test = X_test.drop(columns=['Date'])
print("Being Tested")
clf = SVR(gamma='scale', C=1000.0, epsilon=10,kernel='rbf')
clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
print("Accuracy:",str(clf.score(X_test, y_test)))
print("Error:",str(mean_squared_error(y_pred,y_test)))
# print([y_test,y_pred])


# date = pd.to_datetime(df_ti["Date"])
plt.plot(date,y_pred,color="orange")
plt.plot(date,y_test,color="green")

# plt.plot(date,df_ti['MA_90'],color="red")
plt.xlabel('Date')
plt.ylabel('Price in Rupee')
plt.title("Comparison")
plt.show()

