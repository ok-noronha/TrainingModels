import hashlib
import os

def file_hash(filepath):
    """
    It opens the file at the given path, reads the contents, and returns the MD5 hash of the contents

    :param filepath: The path to the file you want to hash
    :return: The md5 hash of the file.
    """
    with open(filepath, 'rb') as f:
        return md5(f.read()).hexdigest()

#
os.getcwd()
os.chdir(r'C:\Users\oknor\Documents\Programming\TrainingModels\dataset')
os.getcwd()

file_list = os.listdir()
print(len(file_list))

duplicates = []
hash_keys = dict()
for index, filename in  enumerate(os.listdir('.')):
    if os.path.isfile(filename):
        with open(filename, 'rb') as f:
            filehash = hashlib.md5(f.read()).hexdigest()
        if filehash not in hash_keys:
            hash_keys[filehash] = index
        else:
            duplicates.append((index,hash_keys[filehash]))

for index in duplicates:
    os.remove(file_list[index[0]])