import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from pandas.plotting import register_matplotlib_converters
import pandas as pd
from statistical_utility.nse_stocks.sunpharma import SUNPHARMA
from statistical_utility.nse_stocks.pfizer import PFIZER
from statistical_utility.nse_stocks.drreddy import DRREDDY
register_matplotlib_converters()


def direction_accuracy(y_pred,x_test,y_test,l):
    count = 0
    for i in range(0,l):
        if(y_test.iloc[i] >= x_test["Open"].iloc[i]):
            if(y_pred[i] >= x_test["Open"].iloc[i]):
                count = count + 1
        elif(y_test.iloc[i] <= x_test["Open"].iloc[i]):
            if(y_pred[i]<= x_test["Open"].iloc[i]):
                count = count + 1
    acc = count/l
    print("Binary Accuracy:",str(acc))

def get_data(obj=None):
    df = obj.retrieve_inter_day_data()
    df_ti = obj.retrieve_ti()
    df = pd.merge(df,df_ti,on="Date")
    return df

def split_data(obj=None):
    X = get_data(obj)
    X = X.dropna()
    X = X.iloc[-3000:]
    date = X["Date"]
    y = X["Close"]
    X.drop(columns=['Date', '_id_x','_id_y', 'Adj Close','Close'], axis=1, inplace=True)

    today_input = X.iloc[-1]
    X = X.iloc[:-1]
    y = y.iloc[1:]
    date = date.iloc[1:]

    X["Volume"] = X["Volume"]*0.00001
    today_input["Volume"] = today_input["Volume"]*0.00001

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    split = int(0.8 * len(date))
    date = pd.to_datetime(date[split:])

    return X_train, X_test,y_train,y_test,date,today_input

def train_data(X_train,y_train,gamma,C,epsilon):
    clf = SVR(gamma=gamma, C=C, epsilon=epsilon, kernel='rbf')
    clf.fit(X_train, y_train)
    return clf

def test_data(X_test,y_test,clf,today_input,date_test,title):
    y_pred = clf.predict(X_test)
    # print("Accuracy:", str(clf.score(X_test, y_test)))
    print("Error:", str(mean_squared_error(y_pred, y_test)))
    print("Upcoming predicted price:", clf.predict([today_input]))
    direction_accuracy(y_pred, X_test, y_test, len(y_pred))
    plot_data(date_test,y_pred,y_test,title)

def plot_data(date,y_pred,y_test,title):
    plt.plot(date, y_pred, color="blue", label="Predicted Output")
    plt.plot(date, y_test, color="yellow", label="Actual Output")
    legend = plt.legend(loc='upper right', shadow=True, fontsize='x-large')
    legend.get_frame().set_facecolor('C0')

    # plt.plot(date,df_ti['MA_90'],color="red")
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price in Rupee')
    plt.title("Comparison")
    plt.show()


def pred_sunpharma():
    X_train, X_test, y_train, y_test, date_test, today_input = split_data(SUNPHARMA())
    gamma=0.0000000001
    C=7000000
    epsilon=0.06
    title="SUNPHARMA"
    clf = train_data(X_train,y_train,gamma,C,epsilon)
    test_data(X_test, y_test, clf, today_input, date_test,title)
    return None

def pred_pfizer():
    X_train, X_test, y_train, y_test, date_test, today_input = split_data(PFIZER())
    gamma = 0.0000000001
    C = 7000000
    epsilon = 0.06
    title = "PFIZER"
    clf = train_data(X_train, y_train, gamma, C, epsilon)
    test_data(X_test, y_test, clf, today_input, date_test,title)
    return None

def pred_drreddy():
    X_train, X_test, y_train, y_test, date_test, today_input = split_data(DRREDDY())
    gamma = 0.0000000001
    C = 7000000
    epsilon = 0.06
    title = "DRREDDY"
    clf = train_data(X_train, y_train, gamma, C, epsilon)
    test_data(X_test, y_test, clf, today_input, date_test,title)
    return None



if __name__ == "__main__":
    pred_drreddy()
    pred_sunpharma()
    pred_pfizer()



