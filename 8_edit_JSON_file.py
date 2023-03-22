
import json
import glob
import os
import numpy as np

input_folder = r"C:\Users\h.jayasekara\Desktop\math_in_python"
input_fhs=glob.glob(os.path.join(input_folder,'*.json'))
for fh in input_fhs:
    product_name = os.path.split(fh)[-1].split('.json')[0]
    print(product_name)
        
    with open(fh, 'r') as f:
        data = json.load(f)
    
        for year in data:
            # print(year)
            array = []
            
            for d in data[year]:
                array.append(d['mean'])
           
            # array_c = np.array(array, dtype=np.float64)
            maxvalue = max(filter(None.__ne__, array)) 
            minvalue = min(filter(None.__ne__, array)) 
            

            # if maxvalue is not None and minvalue is not None:
            delta = maxvalue - minvalue

            for d in data[year]:
                if d['mean'] is not None:
                    difference = d['mean'] - minvalue
                    normalize = difference / delta
                    d['normalize'] = normalize
                else:
                    normalize = None
                    d['normalize'] = normalize
           
        with open(r"C:\Users\h.jayasekara\Desktop\json_res\{}.json".format(product_name), 'w') as f:
            json.dump(data, f)
        
    

