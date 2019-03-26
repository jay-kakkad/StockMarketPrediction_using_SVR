import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from pandas.plotting import register_matplotlib_converters
import pandas as pd
from numerical_data.nse_stocks.pfizer import PFIZER
from numerical_data.exchanges.nifty50 import NIFTY
register_matplotlib_converters()

pfizer = PFIZER()
nifty = NIFTY()

df_nifty = nifty.retrieve_inter_day_data()
df_nifty.drop(columns=['Date','_id','Volume'], axis=1, inplace=True)
df_nifty.rename(index=str,columns={"High":"Nifty High","Low":"Nifty Low","Open":"Nifty Open","Close":"Nifty Close","Adj Close":"Nifty Close"})
print(df_nifty.head())

df_ti_pf = pfizer.retrieve_ti()
df_ti_pf.drop(columns=['Date','_id','RSI_6','RSI_12'], axis=1, inplace=True)
df_pf = pfizer.retrieve_inter_day_data()
date = df_pf['Date'].iloc[90:-4]
y = df_pf["Close"]
y = y.iloc[90:-4]
print(len(y))
df_pf.drop(columns=['Date','_id','Close'], axis=1, inplace=True)




# df_ti_sensex = sensex.retrieve_ti()
# df_sensex = sensex.retrieve_inter_day_data()
# df_sensex.drop(columns=['Date','_id'], axis=1, inplace=True)
# print(df_sensex)
#
# df_ti_nifty = nifty.retrieve_ti()
# df_nifty = nifty.retrieve_inter_day_data()
# df_nifty.drop(columns=['Date','_id'], axis=1, inplace=True)
# print(df_nifty)


# print(df_ti.columns)

test_parameters = [df_pf.iloc[89:-5],df_ti_pf[89:-5]]
realtime_test = [df_pf.iloc[[-4]],df_ti_pf.iloc[[-4]]]

X = pd.concat(test_parameters,axis=1,sort=False)
print(len(X))
print(X.tail())
test = pd.concat(realtime_test,axis=1)
X["Volume"] = X["Volume"]*0.01
test["Volume"] = test["Volume"]*0.01

X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.1,shuffle=False)
t=0.9
split = int(t*len(date))
date = pd.to_datetime(date[split:])
print("Being Tested")
clf = SVR(gamma=0.0000000025, C=1000000, epsilon=0.1,kernel='rbf')
clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
print("Accuracy:",str(clf.score(X_test, y_test)))
print("Error:",str(mean_squared_error(y_pred,y_test)))
print("Today predicted price:",clf.predict(test))

# print([y_test,y_pred])


# date = pd.to_datetime(df_ti["Date"])
plt.plot(date,y_pred,color="blue",label="Predicted Output")
plt.plot(date,y_test,color="yellow", label="Actual Output")
legend = plt.legend(loc='upper right', shadow=True, fontsize='x-large')
legend.get_frame().set_facecolor('C0')

# plt.plot(date,df_ti['MA_90'],color="red")
plt.xlabel('Date')
plt.ylabel('Price in Rupee')
plt.title("Comparison")
plt.show()


