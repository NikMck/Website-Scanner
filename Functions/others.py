import os

def createDir(directory): #Creates directory
    if not os.path.exists(directory): #If it doesn't exist
        os.makedirs(directory) #It makes it

def writeFile(path, data): #Used to write collected data to a file
    f = open(path, "w") #opens specific file to store data
    f.write(data) #writes it
    f.close() #closes it

