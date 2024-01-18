#Backward_Stepwise Copyright (C) 2023 Bashir Hussein
import pandas as pd
import statsmodels.api as sm

def backward():
    # laadt een excel file in als dataset
    df = pd.read_excel('Backward_non_maatregelen.xlsx')
    # selecteer een kolom(x) als uitkomst, een een range(y) als inputwaarden
    x = df.iloc[:, 5:]
    y = df.iloc[:, 4]

    #Fit de parameters op een OLS model
    model = sm.OLS(y,x)
    results = model.fit()

    
    p_values = results.pvalues
    #selecteer een p-value
    while p_values.max() > 0.5:
        max_pvalue_index = p_values.idxmax()
        x = x.drop(max_pvalue_index, axis=1)
        model = sm.OLS(y,x).fit()
        p_values = model.pvalues
    
    print(model.summary())

if __name__ == '__main__':
    backward()
