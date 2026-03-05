#4
import shutil
shutil.copy('some.txt','any.txt')
#5
import os 
if os.path.exists("any.txt"):
    os.remove("any.txt")
else:
     print("does not exist")