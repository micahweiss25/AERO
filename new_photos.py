''' create a new directory where the photo names are numbered sequentially 
TO DO:
import all photos
put names into a list
iterate through the list, resaving photos with name cooresponding to iteration number
'''
from PIL import Image
import os
new_dir = os.path.join(r"C:\Users\Micah.Weiss\Desktop\AERO", "new")
try:
    os.mkdir(new_dir)
except FileExistsError:
    print('got it')
directory = r"parsed_tomatos"
file_names = []
count = 0
for filename in os.listdir(directory):
    im = Image.open("parsed_tomatos/" + filename)
    im.save(f"./new/photo_{count}.jpg")