import pathlib
for path in pathlib.Path("dict").iterdir():
        if path.is_file():
            f=open(path,"r")
            data=f.read()
            data=data.replace(","," ")
            word=data.split()
        print(len(word))
        
