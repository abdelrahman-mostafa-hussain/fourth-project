import re

def isExistFile(path:str):
    try:
        file= open(f"{path}","r")
        print("file is found")
        return file
    except Exception as noFileFound:
        print("file is not exist")
        return None

def readFile(file:str):
    return file.read()

def removeUnwantChar(content:str):
    return re.sub("[^a-zA-Z0-9\s]","",content)

def countWord(list):
    return len(list)

def main():
    path=input("enter the file path with extension: ")
    file=isExistFile(path)
    if file!=None:
        content=readFile(file)
        new_content:str=removeUnwantChar(content)
        word_list:list=new_content.split(" ")
        count_word:int=countWord(word_list)
        print("the number word in this file is",count_word)
    else:
        print("the number word is 0, becouse the file is not exist")

if __name__=="__main__":
    main()