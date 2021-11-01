import pandas as pd #importing necessary libraries
import json

def count_overweight(bmi=[]):
    count=0
    for i in bmi:
        if 25<=i<=29.9:
            count+=1
    return count

if __name__ == "__main__":

    # data given by you
    data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
    { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
    { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
    { "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
    {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
    {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]

    dict_ = {
        'Gender':[],
        'HeightCm':[],
        'WeightKg':[]
    }

    for i in data:
        for j in i.keys():
            dict_[j].append(i[j])
    
    dataframe = pd.DataFrame(dict_)
  
    dataframe['Heightm'] = dataframe['HeightCm']/100

    dataframe['BMI(kg/m^2)'] = dataframe['WeightKg']/(dataframe['Heightm'] * dataframe['Heightm'])

    dataframe = dataframe.drop('HeightCm',axis=1)

    print(dataframe.head(6))

    print("Total overweight people ",count_overweight(dataframe['BMI(kg/m^2)']))
