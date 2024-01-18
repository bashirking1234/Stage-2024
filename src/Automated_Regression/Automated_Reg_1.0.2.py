#Automated_Regression Copyright (C) 2023 Tom van der Greft
import pickle
import numpy as np
import pandas as pd
from sklearn import tree
from sklearn import ensemble
from sklearn import linear_model
from sklearn import model_selection


def tree_regression():
    param = user_input_string("criterion (squared_error”, “friedman_mse”, "
                              "“absolute_error”, “poisson)\n:")
    mf = user_input_string("Max features (“auto”, “sqrt”, “log2”)\n:")
    rs = user_input_int("random state: default = None\n:")
    msl = user_input_float("min samples leaf: default = 1\n")
    mss = user_input_int("min samples split: default = 2\n")
    mwfl = user_input_float("min weight fraction leaf: default = 0.0\n")
    #min_samples_split=mss,
    model = tree.DecisionTreeRegressor(criterion=param, max_features=mf,
                                       random_state=rs, min_samples_leaf=msl,
                                       min_samples_split=mss,
                                       min_weight_fraction_leaf=mwfl)
    return model

 #  Werk de verschillende modellen uit(Niet compleet)
def adaboost_regression():
    model = ensemble.AdaBoostRegressor()
    return model


def linear_regression():
    model = linear_model.LinearRegression()
    return model


def bayesian_ridge_regression():
    model = linear_model.BayesianRidge()
    return model


def ridge_regression():
    model = linear_model.Ridge()
    return model


def perceptron_regression():
    model = linear_model.Perceptron()
    return model


def passive_agressive_regression():
    model = linear_model.PassiveAggressiveRegressor()
    return model


def poisson_regression():
    model = linear_model.PoissonRegressor()
    return model


def ard_regression():
    model = linear_model.ARDRegression()
    return model


def gamma_regression():
    model = linear_model.GammaRegressor()
    return model


def tweedie_regression():
    model = linear_model.TweedieRegressor()
    return model


def huber_regression():
    model = linear_model.HuberRegressor()
    return model


def bagging_regression():
    estimators = user_input_int("estimators: default = 10\n:")
    maxsamples = user_input_float("max samples: default = 1.0\n:")
    maxfeatures = user_input_float("max features: default = 1.0\n:")
    randomstate = user_input_int("random state: default = None\n:")
    warmstart = user_input_int("warm start: (1/0) default = 1\n:")
    model = ensemble.BaggingRegressor(n_estimators=estimators,
                                      max_samples=maxsamples,
                                      warm_start=warmstart,
                                      random_state=randomstate,
                                      max_features=maxfeatures,

                                      )
    return model


def voting_regression():
    model = ensemble.VotingRegressor()
    return model


def model_fit(model, training_data, y):
    fitted_model = model.fit(training_data, y, )
    return fitted_model


def predict(model, test_data):
    return model.predict(test_data)


def r_sq(model, training_data, predictor_data):
    rsq = model.score(training_data, predictor_data)
    return rsq


def model_select():
    """Selecteer het model waarmee getraint moet worden"""
    print("""        0: tree_regression()
        1: adaboost_regression()
        2: linear_regression()
        3: bayesian_ridge_regression()
        4: ridge_regression()
        5: perceptron_regression()
        6: passive_agressive_regression()
        7: poisson_regression()
        8: ard_regression()
        9: gamma_regression()
        10: tweedie_regression()
        11: huber_regression()
        12: bagging_regression()""")
    choice = user_input_int("Enter Model Number:\n")

    print(choice)
    print(type(choice))
    if choice == 0:
        model = tree_regression()
        return model
    elif choice == 1:
        model = adaboost_regression()
        return model
    elif choice == 2:
        model = linear_regression()
        return model
    elif choice == 3:
        model = bayesian_ridge_regression()
        return model
    elif choice == 4:
        model = ridge_regression()
        return model
    elif choice == 5:
        model = perceptron_regression()
        return model
    elif choice == 6:
        model = passive_agressive_regression()
        return model
    elif choice == 7:
        model = poisson_regression()
        return model
    elif choice == 8:
        model = ard_regression()
        return model
    elif choice == 9:
        model = gamma_regression()
        return model
    elif choice == 10:
        model = tweedie_regression()
        return model
    elif choice == 11:
        model = huber_regression()
        return model

    elif choice == 12:
        model = bagging_regression()
        return model
    # voting regression mist hier nog

    else:
        print("No valid model number given")
        model = model_select()

    return model

def source(text):
    filename = user_input_string(text)
    df = pd.read_excel(filename)

    #x_value = 6:124
    #y_value = 5
    #x_one = user_input_int("First training column")
    #x_two = user_input_int("Last training column")
    #y_one = user_input_int("Predictor column")

    #x = df.iloc[:, x_one:x_two]  # 6:124
    #y = df.iloc[:, y_one]  # 5
    #print(df.iloc[:,3].head())
    x = df.iloc[:, [50, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]]
    #print(x.head())
    y = df.iloc[:, 3]  # 5


    return x, y


def user_input_string(text):
    string = input(text)
    return string


def user_input_int(text):
    number = input(text)
    try:
        number = int(number)
        return number
    except:
        print("Not a number!")
        user_input_int(text)

def user_input_float(text):
    flt = input(text)
    try:
        flt = float(flt)
        return flt
    except:
        print("Not a float!")
        user_input_float(text)


def save_object(path, data):
    with open(path, 'wb') as f:  # open a text file
        pickle.dump(data, f)  # serialize the list
    f.close()
    return


def return_object(path):
    with open(path, 'rb') as f:
        variable = pickle.load(f)  # deserialize using load()
    f.close()
    return variable


def main():
    # Import file/selecteer oud model
    #training_data = np.array([[4, 1], [5, 1], [20, 1], [14, 1], [32, 1],
    #                          [22, 1], [38, 1], [43, 1]])
    # Kolom met de uitkomsten
    #predictor_data = np.array([4, 5, 20, 14, 32, 22, 38, 43])
    # Kolom met waarden die als voorspelling dienen
    #test_data = np.array([[4, 1], [10, 5], [99, 292], [-99, 1]])



    #training_data, predictor_data = source("Filename for training\n")

    # Kies model type (0 to 0)

    # X_train, X_test, y_train, y_test: X = Training data, y = predictor data

    #X_train, X_test, y_train, y_test = model_selection.train_test_split(
    #    training_data, predictor_data, test_size=0.3, random_state=42)

    X_train, y_train = source("Training data")

    X_test, y_test = source("Test data")

    model = model_select()
    print(type(model))
    fitted_model = model_fit(model, X_train, y_train)
    print(predict(fitted_model, X_test))
    print(r_sq(fitted_model, X_test, y_test))
    while True:
        try:
            X_val, y_val = source("Validatie data")
            print("======")
            print(model.predict(X_val))
            return False
        except:
            print("something went wrong")
#[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
#Training: /Users/tomvandergreft/Downloads/MainV3_Training_80.xlsx
#Test: /Users/tomvandergreft/Downloads/MainV3_Test_10.xlsx
#0.6042586913179373
#0.5682675248220743


if __name__ == '__main__':
    main()
