import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, Lasso, LogisticRegression
from sklearn.ensemble import GradientBoostingRegressor, RandomForestClassifier
from sklearn.neural_network import MLPRegressor, MLPClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC, SVR
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

#default test split
test_split = 0.2
random_state = 69 #keep results the same

class Regressors(object):
    def __init__(self, x, y, test_split):
        self.x = x
        self.y = y
        self.x_train, self.x_test, self.y_train, self.y_test = \
        train_test_split(x,y,test_size=test_split, random_state=random_state)
    def __str__(self):
        return (pd.concat([x,y], axis=1))

    def Linear_Regression(self):
        try:
            linreg.fit(self.x_train, self.y_train)
            return [linreg, linreg.score(self.x_test, self.y_test)]
        except:
            raise Exception("Data is invalid for selected model!")

    def Lasso_Regression(self):
        lasso = Lasso()
        try:
            lasso.fit(self.x_train, self.y_train)
            return [lasso, lasso.score(self.x_test, self.y_test)]
        except:
            raise Exception("Data is invalid for selected model!")

    def Gradient_Boosting_Regressor(self):
        gbr = GradientBoostingRegressor()
        try:
            gbr.fit(self.x_train, self.y_train)
            return [gbr, gbr.score(self.x_test, self.y_test)]
        except:
            raise Exception("Data is invalid for selected model!")

    def Support_Vector_Machine(self):
        svr = SVR()
        try:
            svr.fit(self.x_train, self.y_train)
            return [svr, svr.score(self.x_test, self.y_test)]
        except:
            raise Exception("Data is invalid for selected model!")

    def Neural_Network(self):
        nn = MLPRegressor()
        try:
            nn.fit(self.x_train, self.y_train)
            return [nn, nn.score(self.x_test, self.y_test)]
        except:
            raise Exception("Data is invalid for selected model!")

class Classifiers(object):
    def __init__(self, x, y):
        le = LabelEncoder()
        self.x = x
        self.y = y
        self.x_train, self.x_test, self.y_train, self.y_test = \
            train_test_split(x, le.fit_transform(y), test_size=test_split,
                             random_state=random_state)
    def __str__(self):
        return pd.concat([self.x,self.y], axis=1)

    def Logistic_Regression(self):
        lr = LogisticRegression()
        try:
            lr.fit(self.x_train, self.y_train)
            return [lr, lr.score(self.x_test, self.y_test)]
        except:
            raise Exception("Data is invalid for selected model!")

    def Support_Vector_Machine(self):
        svc = SVC()
        try:
            svc.fit(self.x_train, self.y_train)
            return [svc, svc.score(self.x_test, self.y_test)]
        except:
            raise Exception("Data is invalid for selected model!")

    def K_Nearest_Neighbors(self):
        knn = KNeighborsClassifier()
        try:
            knn.fit(self.x_train, self.y_train)
            return [knn, knn.score(self.x_test, self.y_test)]
        except:
            raise Exception("Data is invalid for selected model!")

    def Random_Forests(self):
        rfc = RandomForestClassifier()
        try:
            rfc.fit(self.x_train, self.y_train)
            return [rfc, rfc.score(self.x_test, self.y_test)]
        except:
            raise Exception("Data is invalid for selected model!")

    def Neural_Network(self):
        nn = MLPClassifier(hidden_layer_sizes=(50, 50), learning_rate_init=0.01, batch_size='auto',
                           nesterovs_momentum=False)
        try:
            nn.fit(self.x_train, self.y_train)
            return [nn, nn.score(self.x_test, self.y_test)]
        except:
            raise Exception("Data is invalid for selected model!")

def get_relevant_dataset(x, y, dataset):
    '''
    :param x: list of strings of x-columns
    :param y: string with name of y-column
    :param dataset: pandas dataframe
    :return: x ndarray and y ndarray
    '''
    assert(isinstance(x, list))
    assert(isinstance(y, str))
    df_x = dataset[x]
    df_y = dataset[y]
    return df_x.values, df_y.values

def get_models(x_, y_, dataset, regression = True):
    (x,y) = get_relevant_dataset(x_, y_, dataset)
    if regression:
        base = Regressors(x, y)
        attrs = [method_name for method_name in dir(base) if callable(getattr(base, method_name))][:5] #from stackoverflow
        model_names = [i.replace("_", " ") for i in attrs]
        return model_names, base
    else:
        base = Classifiers(x, y)
        attrs = [method_name for method_name in dir(base) if callable(getattr(base, method_name))][:5]  # from stackoverflow
        model_names = [i.replace("_", " ") for i in attrs]
        return model_names, base

def run_model(model_name, base_class):
    pass