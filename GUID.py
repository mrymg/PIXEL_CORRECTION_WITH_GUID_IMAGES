import uuid
import os


def pid():
    return uuid.uuid4()

path = "/Users/ymg/Desktop/BBM/BBM 419/final_197/"
names = list()
for file in os.listdir(path):
    names.append(file)

names.sort()

for i in range(0, len(names), 2):
    idm = pid()
    os.rename(path + names[i], '/Users/ymg/Desktop/BBM/BBM 419/guided3/' + str(idm) + '.png')
    os.rename(path + names[i+1], '/Users/ymg/Desktop/BBM/BBM 419/guided3/' + str(idm) + '_L.png')