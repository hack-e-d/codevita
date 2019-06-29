t=int(input())
while t!=0:
    n=input().split(" ")
    n1=int(n[0])
    n2=int(n[1])
    a=0
    b=0
    min=n1*(-10000000)+n2*10000000
    for i in range(-10000000,10000000):
        for j in range(-10000000,10000000):
            x=n1*i+n2*j
            if(x>0 and x<min):
                a=i
                b=j
                min=x
    print(min)
    t-=1
