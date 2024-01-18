#Firenze Lokaal Copyright (C) 2023 Tom van der Greft
import joblib
import numpy as np
import pandas as pd
#Laadt de preprocessor in, deze doet nu niks, maar als deze werkend te krijgen is is dat een grote bonus
ct = joblib.load("/Users/tomvandergreft/Downloads/TAR_DOWNLOADTEST_P112_E7018"
                "/preprocessor.joblib")


#Laadt een excel file in als dataset.
path = '/Users/tomvandergreft/Downloads/Main_Download.xlsx'
def excel_to_data(path):
    df = pd.read_excel(path, sheet_name='Training-100')
    data = df.loc[:,
        'New_cases':'Coverage_repeat_vaccination_autumn_round_wk3_2010']
    print(data)


    return data

data = excel_to_data(path)





"""Test data, 
data = ([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [0]])
i = 0
while i < 113:
    data[0].append(1)
    data[1].append(2)
    data[2].append(3)
    data[3].append(4)
    data[4].append(5)
    data[5].append(6)
    data[6].append(7)
    data[7].append(8)
    data[8].append(9)
    data[9].append(10)
    data[10].append(0)
    i+=1
"""
#visualiseer de data
print(len(data))
print(data)

#Laadt het model in
model_1 = joblib.load(
    "/Users/tomvandergreft/Downloads/TAR_DOWNLOADTEST_P112_E7018"
                      "/classifier.joblib")
#predict met de data op het model
answer1 = model_1.predict(data)

#deze formule werkt voor een samenstelling van de covid dataset met het bagging model.
#De volgore van de parameters is echter niet duidelijk.
true_answer = ((answer1 -1748.8904)/2.2592)

i = 0
while i < len(answer1):
    print(str((i+1)))
    print(answer1[i])
    print(true_answer[i])
    i += 1
# Print diagnostiche data over het model
print(type(model_1))
print(model_1.get_params())
