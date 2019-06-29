def fact(n):
    if(n>1):
        return int(n)*fact(int(n-1))
    else:
        return int(1)
n=int(input())
a=input().split(" ")
b=[0]
h=1
mod=1000000007
for s in a:
    b.append(int(s))
y=[]
z=[]
q=int(input())
for i in range(0,q):
    ww=input().split(" ")
    y.append(int(ww[0]))
    z.append(int(ww[1]))
for i in range(0,q):
    l=int(y[i])
    r=int(z[i])
    for j in range(l,r+1):
        h*=fact(int(b[j]))
    h=h%mod
    h=h**(r-l)
    print(h)

