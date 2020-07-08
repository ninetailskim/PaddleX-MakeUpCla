import glob
import random

mydata = glob.glob(".\\demakeup\\*.jpg")

random.shuffle(mydata)

print(mydata)

trainindex = round(len(mydata) * 0.8)
valindex = round(len(mydata) * 0.95)

with open("train_list.txt", 'a') as fp:
    for imgPath in mydata[:trainindex]:
        imgPath = imgPath.split("\\")
        print(imgPath)
        imgPath = "/".join(imgPath)
        print(imgPath)
        fp.write(imgPath + " 7\n")


with open("val_list.txt", 'a') as fp:
    for imgPath in mydata[trainindex:valindex]:
        imgPath = imgPath.split("\\")
        print(imgPath)
        imgPath = "/".join(imgPath)
        print(imgPath)
        fp.write(imgPath + " 7\n")

with open("test_list.txt", 'a') as fp:
    for imgPath in mydata[valindex:]:
        imgPath = imgPath.split("\\")
        print(imgPath)
        imgPath = "/".join(imgPath)
        print(imgPath)
        fp.write(imgPath + " 7\n")