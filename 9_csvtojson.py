import csv
import pandas as pd
import json
import re

data = {}
year=[]



# selected_folder  = r""
# input_files = glob(os.path.join(selected_folder, '*.csv'))

# for files in input_files:
#     json_name = os.path.split(files)[-1].split('csv')[0]


a =r'C:\Users\h.jayasekara\Desktop\q1111.csv' 


columns = ["id", "mean_2015", "mean_2016", "mean_2017", "mean_2018", "mean_2019", "mean_2020", "mean_2021"]
df = pd.read_csv(a, usecols=columns)

for col in df.columns:
    if(bool(re.match('mean',col))):
        yr= col.split('_')[1]
        year.append(yr)    
        
        values = []
        
        for index, row in df.iterrows():
            id_val = row['id']
            mean_val = row['mean_{}'.format(yr)]
            values.append({'id': id_val, 'mean': mean_val})
        data[yr] = values
print(data) 
            

    
