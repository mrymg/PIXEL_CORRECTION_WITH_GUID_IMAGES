import uuid
import os


def pid():
    return uuid.uuid4()

SOURCE = "SOURCE PATH FOR TO GUID IMAGES"
DST = "DESTINATION PATH TO NEW IMAGES"

names = list()
for file in os.listdir(SOURCE):
    names.append(file)

names.sort()

for i in range(0, len(names), 2):
    idm = pid()
    os.rename(SOURCE + names[i], DST + str(idm) + '.png')
    os.rename(SOURCE + names[i+1], DST + str(idm) + '_L.png')
