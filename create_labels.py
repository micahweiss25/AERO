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


directory = r"C:\Users\Micah.Weiss\OneDrive - West Point\AY 22-2\CS485\PROJECT\parsed_tomatos"
ids = []
for filename in os.listdir(directory):
    ids.append(int(filename[:filename.find("_")]))
# ids becomes a list of all the "id" in the json file

















with open("C:\\Users\Micah.Weiss\OneDrive - West Point\AY 22-2\CS485\PROJECT\laboro_tomato\laboro_tomato\\annotations\\test.json", "r") as f:
    file = f.read()
images_index = file.index('"images" : [')
annotations_index = file.index('"annotations" : [')
images = file[images_index:annotations_index].replace("\n","")
annotations = file[annotations_index:].replace(" ", "").replace("\n", "")
annotations_list = annotations.split("{")
annotations_list = annotations_list[1:]
print(len(annotations))




def create_data_list():
    sweet_data =[]
    for i in annotations_list:
        id = i[i.index('"id":')+len('"id":'):i.index("}",i.index('"id":')+len('"id":'))]
        cat = i[i.index('"category_id":')+len('"category_id"')+1:i.index(',',i.index('"category_id":')+len('"category_id"'))]
        sweet_data.append([int(id),int(cat)])
    return sweet_data
data = create_data_list()
print(len(data))
var =[]
for i in data:
    if i[0] in ids:
        var.append(i)

print(len(var))
print(len(ids))
'''
id_cat = []
print(data[:20])
for i in data:
    if ids.count(i[0]) > 0:
        id_cat.append(i)
    
print(data[:40])
print(ids[:5])'''