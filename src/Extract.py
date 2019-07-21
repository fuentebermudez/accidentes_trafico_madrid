import os
import pandas as pd

os.chdir(r"..\\Data")
directory=os.curdir
files=os.listdir(directory)
files=[directory+ '\\' +file for file in files]
data=[]
for file in files:
    print(file)
    content=pd.read_excel(file)
    data.append(content)
merged_data=pd.concat(data)
