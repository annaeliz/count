from pathlib import Path
basepath = Path(input("Please enter the Folder name: "))
def countword(basepath):
    files_in_basepath = basepath.iterdir()
    for item in files_in_basepath:
        if item.is_file():
            print(item.name)
            try:
                f=open(item,"r")
                data=f.read()
                data=data.replace(","," ")
                word=data.split()
                print(item,"-", len(word))
            except UnicodeDecodeError:
                pass
                print("Please enter vaild File/Folder name")
    return(basepath)
print(countword(basepath))   

