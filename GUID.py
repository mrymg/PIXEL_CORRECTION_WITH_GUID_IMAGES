import uuid
import os


def pid():
    return uuid.uuid4()

path = "C:\\Users\\ymgoz\\Desktop\\assigned-to-yunus2\\WITH_PIXEL_CORRECTION\\final_197_son\\"
names = list()
for file in os.listdir(path):
    names.append(file)

names.sort()

for i in range(0, len(names), 2):
    idm = pid()
    os.rename(path + names[i], 'C:\\Users\\ymgoz\\Desktop\\assigned-to-yunus2\\WITH_PIXEL_CORRECTION\\GUIDED_3\\' + str(idm) + '.png')
    os.rename(path + names[i+1], 'C:\\Users\\ymgoz\\Desktop\\assigned-to-yunus2\\WITH_PIXEL_CORRECTION\\GUIDED_3\\' + str(idm) + '_L.png')
