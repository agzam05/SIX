#1
a=int(input())
arr=list(map(int, input().split()))
def square(x):
    return x*x
ar=list(map(square, arr))
print(ar)
#2
from functools import reduce
a=int(input())
arr=list(map(int, input().split()))
ar=reduce(lambda x,y:x+y,arr)
print(ar)
#3
a=int(input())
arr=list(map(int, input().split()))
def even(x):
    return x%2==0
ar=list(filter(even, arr))
print(ar)
