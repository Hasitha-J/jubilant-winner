import json

json_input = open(r"C:\Users\h.jayasekara\Desktop\math_in_python/AETI_adm1.json")

data = json.load(json_input)

for year in data:
    # print(year)
    array = []
    
    for d in data[year]:
        array.append(d['mean'])
    
    maxvalue = max(array) 
    minvalue = min(array)
    
    delta = maxvalue - minvalue
    
    for d in data[year]:
        difference = d['mean'] - minvalue
        normalize = difference / delta
        d['normalize'] = normalize


with open(r"C:\Users\h.jayasekara\Desktop\math_in_python\normalized_data.json", 'w') as f:
    json.dump(data, f)
    
