import os
import datetime


myPath = os.getcwd()
files = os.listdir(myPath)
for f in files:
    if f.startswith("NET") :
        print(f)
        fx=open(f)
        lines=fx.readlines()
        fx.close()
        data = (for i in lines i.split(",")
        print(data)
