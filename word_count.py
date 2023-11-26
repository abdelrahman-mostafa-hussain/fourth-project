def isExistFile(path):
    try:
        file= open(f"{path}","r")
        print("file is found")
        return file
    except Exception as noFileFound:
        print("file is not exist")
        return None

def main():
    path=input("enter the file path: ")
    file=isExistFile(path)

if __name__=="__main__":
    main()