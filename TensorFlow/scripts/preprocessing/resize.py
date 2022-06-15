from PIL import Image
import os, sys

path = "C:\\Users\\oknor\\Documents\\Programming\\TrainingModels\\TensorFlow\\workspace\\car_training\\images\\"
dirs = os.listdir( path )
final_size = 320;

def resize(asr):
    count=0
    for item in dirs:

        if os.path.isfile(path+item):
            f, e = os.path.splitext(item)
            if(f=='resize'):
                continue
            im = Image.open(path+item)
            size = im.size
            ratio = float(final_size) / max(size)
            new_image_size = tuple([int(x*ratio) for x in size])
            imResize = im.resize(new_image_size, Image.ANTIALIAS)
            imRGB= Image.new('RGB', (final_size, final_size), (255, 255, 255))
            imRGB.paste(imResize, ((final_size-new_image_size[0])//2, (final_size-new_image_size[1])//2))
            if count%9==0 :
                imRGB.save(path+"test\\car_%3d.jpg"%count, 'JPEG', quality=90)
            else:
                imRGB.save(path+"train\\car_%3d.jpg"%count, 'JPEG', quality=90)
            count+=1
        else:
            print ("Could not find")

resize(True)
