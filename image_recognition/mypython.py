import os
os.chdir("C:\\Multiplechoicequestions\\ImageSets")
os.mkdir("test")
os.mkdir("train")
os.mkdir("val")
os.chdir(".\\test")

file_jpeg = os.listdir("C:\\Multiplechoicequestions\\JPEGImages\\test")
file_anno = os.listdir("C:\\Multiplechoicequestions\\Annotations\\test")
with open("C:\\Multiplechoicequestions\\ImageSets\\test\\test.txt", 'w') as f:
    for i in file_jpeg:
        f.write("..\\JPEGImages\\test\\"+str(i)+' '+"..\\Annotations\\test"+str(i).replace('png', 'xml')+'\n')


file_jpeg = os.listdir("C:\\Multiplechoicequestions\\JPEGImages\\train")
file_anno = os.listdir("C:\\Multiplechoicequestions\\Annotations\\train")
with open("C:\\Multiplechoicequestions\\ImageSets\\train\\train.txt", 'w') as f:
    for i in file_jpeg:
        f.write("..\\JPEGImages\\train\\" + str(i) + ' ' + "..\\Annotations\\train" + str(i).replace('png', 'xml') + '\n')


file_jpeg = os.listdir("C:\\Multiplechoicequestions\\JPEGImages\\val")
file_anno = os.listdir("C:\\Multiplechoicequestions\\Annotations\\val")
with open("C:\\Multiplechoicequestions\\ImageSets\\val\\val.txt", 'w') as f:
    for i in file_jpeg:
        f.write("..\\JPEGImages\\val\\"+str(i)+' '+"..\\Annotations\\val"+str(i).replace('png', 'xml')+'\n')
