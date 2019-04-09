import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from pandas.plotting import register_matplotlib_converters
import pandas as pd
from statistical_utility.nse_stocks.sunpharma import SUNPHARMA
register_matplotlib_converters()

def get_data():
    sp = SUNPHARMA()
    df = sp.retrieve_inter_day_data()
    df_ti = sp.retrieve_ti()
    df = pd.merge(df,df_ti,on="Date")
    return df

def split_data():
    X = get_data()
    X = X.dropna()
    print(X.head())
    date = X["Date"]
    y = X["Close"]
    X.drop(columns=['Date', '_id_x','_id_y', 'Adj Close','Close'], axis=1, inplace=True)

    today_input = X.iloc[-1]

    X = X.iloc[:-1]
    y = y.iloc[1:]

    X["Volume"] = X["Volume"] * 0.01
    today_input["Volume"] = today_input["Volume"] * 0.01

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, shuffle=False)
    split = int(0.75 * len(date))
    date = pd.to_datetime(date[split:])

    return X_train, X_test,y_train,y_test,date,today_input

def train_data(X_train,y_train):
    clf = SVR(gamma=0.0000000025, C=1000000, epsilon=0.1, kernel='rbf')
    clf.fit(X_train, y_train)
    return clf

def test_data(X_test,y_test,clf,today_input,date_test):
    y_pred = clf.predict(X_test)
    print("Accuracy:", str(clf.score(X_test, y_test)))
    print("Error:", str(mean_squared_error(y_pred, y_test)))
    print("Today predicted price:", clf.predict(today_input))
    plot_data(date_test,y_pred,y_test)

def plot_data(date,y_pred,y_test):
    plt.plot(date, y_pred, color="blue", label="Predicted Output")
    plt.plot(date, y_test, color="yellow", label="Actual Output")
    legend = plt.legend(loc='upper right', shadow=True, fontsize='x-large')
    legend.get_frame().set_facecolor('C0')

    # plt.plot(date,df_ti['MA_90'],color="red")
    plt.xlabel('Date')
    plt.ylabel('Price in Rupee')
    plt.title("Comparison")
    plt.show()


if __name__ == "__main__":
    X_train, X_test,y_train,y_test,date_test,today_input = split_data()
    # print(X_train)
    clf = train_data(X_train,y_train)
    test_data(X_test,y_test,clf,today_input,date_test)



