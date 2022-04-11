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
import numpy as np
import os.path
j = json.load(open('test.json'))
jt  = json.load(open('train.json'))
a = np.array([])
b = np.array([])
for i in sorted(jt['annotations'], key=lambda x : x['id']):
    d = i['id']
    if os.path.isfile(f'parsed_tomatos/{d}_tomato.jpg'):
        a = np.append(a,i['category_id'])
for i in sorted(j['annotations'], key=lambda x : x['id']):
    d = i['id']
    if os.path.isfile(f'parsed_tomatos_test/{d}_tomato.jpg'):
        b = np.append(b,i['category_id'])
np.savetxt('annotations_train_category_id.npy',a)
np.savetxt('annotations_test_category_id.npy',b)
print(a)
