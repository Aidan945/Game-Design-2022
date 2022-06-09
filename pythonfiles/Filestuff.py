# Aidan Zarski
# program about using Files, datetime
# 'r' read
# 'a' append
# 'w' write
# open a file and make sure you close it
import random
import os, datetime
from this import d

os.system('cls')

date = datetime.datetime.now()
print(date)
print(date.strftime('%m / %d/ %y'))

name="Aidan"
sce=344
scrLile=str(sce)+"\t"+date.strftime('%m / %d/ %y')+"\t"+name +"\n"
print(scrLile)

#create a file
myFile=open("scre.txt", 'w')
myFile.write(scrLile)
myFile.close()
# Create new line
name = "Peter"
sce=132
scrLile=str(sce)+"\t"+date.strftime('%m / %d/ %y')+"\t"+name 
myFile=open("scre.txt", 'a')
myFile.write(scrLile)
myFile.close()
# read the file
myFile = open("scre.txt","r")
stuff = myFile.readlines()
myFile.close()
for line in stuff:
    print(line)






