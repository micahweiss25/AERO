import os

'''
File
-> photos in file
-> form = #_tomato
-> # corrisponds to an id
-> id has a ripeness value
'''

labels = []

# create array of id: #, ripeness: value
# for file name in dirctory
directory = r"parsed_tomatos"
ids = []
for filename in os.listdir(directory):
    ids.append(int(filename[:filename.find("_")]))
# ids becomes a list of all the "id" in the json file

import json
j = json.load(open('test.json'))
jt  = json.load(open('train.json'))
a = []
for i in j['annotations']:
    a.append(i['category_id'])
print(a)
