import os
import shutil

path = "C:\\Users\\oknor\\Documents\\Programming\\TrainingModels\\dataset\\"
dest_path = "C:\\Users\\oknor\\Documents\\Programming\\TrainingModels\\TensorFlow\\workspace\\car_training\\images\\"
dirs = os.listdir( path )

count=1
for item in dirs:
    if os.path.isfile(path+item):
        f, e = os.path.splitext(item)
        shutil.move(path+item,dest_path+("car_%d"%count)+e)
        count=count+1
    continue