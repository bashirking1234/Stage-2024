#Firenze Local Decoder Copyright (C) 2023 Tom van der Greft
import joblib
import numpy as np
import pandas as pd
#ct = joblib.load("/Users/tomvandergreft/Downloads/TAR_DOWNLOADTEST_P112_E7018""/preprocessor.joblib")


#Laadt een excel file in als dataset.
path = 'Main_Download.tsv'
def excel_to_data(path):
    df = pd.read_excel(path, sheet_name='Training-100')
    data = df.loc[:,
        'New_cases':'Coverage_repeat_vaccination_autumn_round_wk3_2010']
    print(data)




    return data

def tsv_to_sorted(path):
    column_list = ["HBO", "KDV", "MBO", "UNI", "Sport", "Bezoek", "Horeca", "Lockdown", "Winkels ", "1.5 Meter", "Avondklok", "Mondkapje", "New_cases", "New_deaths", "Basisschool", "Thuiswerken", "windrichting", "Contactberoepen", "RWD Zwolle 4026", "RWD Utrcht 10009", "RWD Venray 30020", "zonneschijn tijd", "Middelbare school", "RWD Nijmegen 9024", "RWD Apeldoorn 8022", "RWD Roermond 30024", "Maximum temperatuur", "Mininum Temperatuur", "RWD Den Bosch 27008", "RWD Eindhoven 27003", "RWD Hilversum 11004", "RWD Leeuwarden 2011", "90+-Ziekenuisopnames", "Normalized_New_cases", "maximale vochtigheid", "minimale vochtigheid", "Normalized_New_deaths", "0-14-Ziekenhuisopnames", "20-24-Ziekenuisopnames", "25-29-Ziekenuisopnames", "30-34-Ziekenuisopnames", "35-39-Ziekenuisopnames", "40-44-Ziekenuisopnames", "45-49-Ziekenuisopnames", "50-54-Ziekenuisopnames", "55-59-Ziekenuisopnames", "60-64-Ziekenuisopnames", "65-69-Ziekenuisopnames", "70-74-Ziekenuisopnames", "75-79-Ziekenuisopnames", "80-84-Ziekenuisopnames", "85-89-Ziekenuisopnames", "15-19-Ziekenhuisopnames", "Normalized_windrichting", "Unknown-Ziekenuisopnames", "IC_Bedden_Covid_Nederland", "Normalized_RWD Zwolle 4026", "Etmaal gemiddelde bewolking", "Normalized_RWD Utrcht 10009", "Normalized_RWD Venray 30020", "Normalized_zonneschijn tijd", "Normalize_RWD Apeldoorn 8022", "Normalized_RWD Nijmegen 9024", "Normalize_RWD Den Bosch 27008", "Normalized_RWD Roermond 30024", "IC_Bedden_COVID_Internationaal", "Normalized_Maximum temperatuur", "Normalized_Mininum Temperatuur", "Normalized_RWD Eindhoven 27003", "Normalized_RWD Hilversum 11004", "Normalized_RWD Leeuwarden 2011", "Normalized_90+-Ziekenuisopnames", "Normalized_maximale vochtigheid", "Normalized_minimale vochtigheid", "Coverage_primary_partly_wk1_1960", "Coverage_primary_partly_wk1_2010", "Coverage_primary_partly_wk2_1960", "Coverage_primary_partly_wk2_2010", "Coverage_primary_partly_wk3_1960", "Coverage_primary_partly_wk3_2010", "Normalized_0-14-Ziekenuisopnames", "Normalized_15-19-Ziekenuisopnames", "Normalized_20-24-Ziekenuisopnames", "Normalized_25-29-Ziekenuisopnames", "Normalized_30-34-Ziekenuisopnames", "Normalized_35-39-Ziekenuisopnames", "Normalized_40-44-Ziekenuisopnames", "Normalized_45-49-Ziekenuisopnames", "Normalized_50-54-Ziekenuisopnames", "Normalized_55-59-Ziekenuisopnames", "Normalized_60-64-Ziekenuisopnames", "Normalized_65-69-Ziekenuisopnames", "Normalized_70-74-Ziekenuisopnames", "Normalized_75-79-Ziekenuisopnames", "Normalized_80-84-Ziekenuisopnames", "Normalized_85-89-Ziekenuisopnames", "Coverage_primary_completed_wk1_1960", "Coverage_primary_completed_wk1_2010", "Coverage_primary_completed_wk2_1960", "Coverage_primary_completed_wk2_2010", "Coverage_primary_completed_wk3_1960", "Coverage_primary_completed_wk3_2010", "Normalized_Unknown-Ziekenuisopnames", "minimum temperatuur op 10 cm hoogte", "Normalized_IC_Bedden_Covid_Nederland", "Normalized_Etmaal gemiddelde bewolking", "Normalized_IC_Bedden_COVID_Internationaal", "Normalized_minimum temperatuur op 10 cm hoogte", "Coverage_repeat_vaccination_autumn_round_wk1_1960", "Coverage_repeat_vaccination_autumn_round_wk1_2010", "Coverage_repeat_vaccination_autumn_round_wk2_1960", "Coverage_repeat_vaccination_autumn_round_wk2_2010", "Coverage_repeat_vaccination_autumn_round_wk3_1960", "Coverage_repeat_vaccination_autumn_round_wk3_2010"]
    #2.54356e+186 opties
    #https://rowannicholls.github.io/python/curve_fitting/linear_comparison.html
    #Het aantal opties om door te testen en de file space voor de lijst met
    # al deze opties zijn onmogelijk te behalen.
    data = pd.read_table(path, usecols=column_list)
    print(data)
    data = data.reindex(columns=column_list)
    print(data)
    return data

data = tsv_to_sorted(path)

"""
#Genereer test data
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
#data = pd.DataFrame(data, columns=['New_cases', 'Normalized_New_cases',
# 'New_deaths', 'Normalized_New_deaths', 'IC_Bedden_Covid_Nederland', 'Normalized_IC_Bedden_Covid_Nederland', 'IC_Bedden_COVID_Internationaal', 'Normalized_IC_Bedden_COVID_Internationaal', '0-14-Ziekenhuisopnames', '15-19-Ziekenhuisopnames', '20-24-Ziekenuisopnames', '25-29-Ziekenuisopnames', '30-34-Ziekenuisopnames', '35-39-Ziekenuisopnames', '40-44-Ziekenuisopnames', '45-49-Ziekenuisopnames', '50-54-Ziekenuisopnames', '55-59-Ziekenuisopnames', '60-64-Ziekenuisopnames', '65-69-Ziekenuisopnames', '70-74-Ziekenuisopnames', '75-79-Ziekenuisopnames', '80-84-Ziekenuisopnames', '85-89-Ziekenuisopnames', '90+-Ziekenuisopnames', 'Unknown-Ziekenuisopnames', 'Normalized_0-14-Ziekenuisopnames', 'Normalized_15-19-Ziekenuisopnames', 'Normalized_20-24-Ziekenuisopnames', 'Normalized_25-29-Ziekenuisopnames', 'Normalized_30-34-Ziekenuisopnames', 'Normalized_35-39-Ziekenuisopnames', 'Normalized_40-44-Ziekenuisopnames', 'Normalized_45-49-Ziekenuisopnames', 'Normalized_50-54-Ziekenuisopnames', 'Normalized_55-59-Ziekenuisopnames', 'Normalized_60-64-Ziekenuisopnames', 'Normalized_65-69-Ziekenuisopnames', 'Normalized_70-74-Ziekenuisopnames', 'Normalized_75-79-Ziekenuisopnames', 'Normalized_80-84-Ziekenuisopnames', 'Normalized_85-89-Ziekenuisopnames', 'Normalized_90+-Ziekenuisopnames', 'Normalized_Unknown-Ziekenuisopnames', 'Thuiswerken', 'Lockdown', 'Avondklok', 'KDV', 'Basisschool', 'Middelbare school', 'MBO', 'HBO', 'UNI', 'Mondkapje', '1.5 Meter', 'Horeca', 'Winkels ', 'Sport', 'Contactberoepen', 'Bezoek', 'windrichting', 'Normalized_windrichting', 'Mininum Temperatuur', 'Normalized_Mininum Temperatuur', 'Maximum temperatuur', 'Normalized_Maximum temperatuur', 'minimum temperatuur op 10 cm hoogte', 'Normalized_minimum temperatuur op 10 cm hoogte', 'zonneschijn tijd', 'Normalized_zonneschijn tijd', 'Etmaal gemiddelde bewolking', 'Normalized_Etmaal gemiddelde bewolking', 'maximale vochtigheid', 'Normalized_maximale vochtigheid', 'minimale vochtigheid', 'Normalized_minimale vochtigheid', 'RWD Apeldoorn 8022', 'Normalize_RWD Apeldoorn 8022', 'RWD Den Bosch 27008', 'Normalize_RWD Den Bosch 27008', 'RWD Eindhoven 27003', 'Normalized_RWD Eindhoven 27003', 'RWD Hilversum 11004', 'Normalized_RWD Hilversum 11004', 'RWD Leeuwarden 2011', 'Normalized_RWD Leeuwarden 2011', 'RWD Nijmegen 9024', 'Normalized_RWD Nijmegen 9024', 'RWD Roermond 30024', 'Normalized_RWD Roermond 30024', 'RWD Utrcht 10009', 'Normalized_RWD Utrcht 10009', 'RWD Venray 30020', 'Normalized_RWD Venray 30020', 'RWD Zwolle 4026', 'Normalized_RWD Zwolle 4026', 'Coverage_primary_partly_wk1_1960', 'Coverage_primary_completed_wk1_1960', 'Coverage_repeat_vaccination_autumn_round_wk1_1960', 'Coverage_primary_partly_wk1_2010', 'Coverage_primary_completed_wk1_2010', 'Coverage_repeat_vaccination_autumn_round_wk1_2010', 'Coverage_primary_partly_wk2_1960', 'Coverage_primary_completed_wk2_1960', 'Coverage_repeat_vaccination_autumn_round_wk2_1960', 'Coverage_primary_partly_wk2_2010', 'Coverage_primary_completed_wk2_2010', 'Coverage_repeat_vaccination_autumn_round_wk2_2010', 'Coverage_primary_partly_wk3_1960', 'Coverage_primary_completed_wk3_1960', 'Coverage_repeat_vaccination_autumn_round_wk3_1960', 'Coverage_primary_partly_wk3_2010', 'Coverage_primary_completed_wk3_2010', 'Coverage_repeat_vaccination_autumn_round_wk3_2010'])

print(len(data))
model_1 = joblib.load(
    "/Users/tomvandergreft/Downloads/TAR_DOWNLOADTEST_P112_E7018"
                      "/classifier.joblib")
answer1 = model_1.predict(data)


true_answer = ((answer1 -1748.8904)/2.2592)

i = 0
while i < len(answer1):
    #print(str((i+1)))
    print(answer1[i])
    #print(true_answer[i])
    i += 1
print(type(model_1))
print(model_1.get_params())
