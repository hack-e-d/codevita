from itertools import permutations
def convert(list):
    d=0
    for q in range(0,i):
        d=d*10
        d=d+int(list[q])
    return d
a,b=input().split(" ")
g=[]
i=0
final=[]
c=int(a)
while c!=0:
    r=int(c%10)
    g.append(r)
    i+=1
    c=int(c/10)
prem=permutations(g)
for k in list(prem):
    final.append(convert(k))
min=final[0]
for k in final:
    if(k>int(b) and k<min):
        min=k
if(min>=int(b)):
    print(int(min))
else:
    print(-1)