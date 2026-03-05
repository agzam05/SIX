#4
a=list(map(str, input().split()))
for x,y in enumerate(a):
    print(f"{x}: {y}")
#5
a=list(map(str, input().split()))
b=list(map(str, input().split()))
c=zip(a,b)
for i in c:
    print(i)
