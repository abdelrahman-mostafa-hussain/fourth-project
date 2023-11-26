import re

def isExistFile(path):
    try:
        file= open(f"{path}","r")
        print("file is found")
        return file
    except Exception as noFileFound:
        print("file is not exist")
        return None

def readFile(file):
    return file.read()

def removeUnwantChar(content):
    return re.sub("[^a-zA-Z0-9\s]","",content)

def main():
    path=input("enter the file path: ")
    file=isExistFile(path)
    if file!=None:
        content=readFile(file)
        

if __name__=="__main__":
    main()