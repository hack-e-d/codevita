def fact(n):
    if(n>1):
        return n*fact(int(n-1))
    else:
        return int(1)
n=int(input())
a=input().split(" ")
y,z=[]
q=int(input())
for i in range(0,q):
    y[i],z[i]=input().split(" ")
