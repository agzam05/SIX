#1
import re
a=input()
arr=re.fullmatch("[a][b]*",a)
if arr:
    print(arr.group())
else:
    print("none")
#2
import re
a=input()
arr=re.fullmatch("[a][b]{3}",a)
ar=re.fullmatch("[a][b]{2}",a)
if arr:
    print(arr.group())
elif ar:
    print(ar.group())
else:
    print("none")
#3
import re
a=input()
arr=re.findall(r"^[a-z]+_[a-z]+",a)
print(arr)
#4
import re
a=input()
arr=re.findall(r"[A-Z]+[a-z]+",a)
print(arr)
#5
import re
a=input()
arr=re.findall("^[a]+\w*[b]$",a)
print(arr)
#6
import re
a=input()
arr=re.sub("[.]",":",a)
arr=re.sub("[,]",":",a)
arr=re.sub("[ ]",":",a)
print(arr)
#7
