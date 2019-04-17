import os

def getWorkingDirectory():
    #call get current working directory
    return os.getcwd()

def changeWorkingDirectory(directory = 'C:\\'):
    #changes working directory
    os.chdir(directory)
    return os.getcwd()
