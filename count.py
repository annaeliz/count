import pathlib
for path in pathlib.Path("dict").iterdir():
        if path.is_file():
            try:
                f=open(path,"r")
                data=f.read()
                data=data.replace(","," ")
                word=data.split()
                print(path,len(word))
            except UnicodeDecodeError:
                pass
        
