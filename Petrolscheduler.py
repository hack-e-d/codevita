a = input().split(" ")
for i in range(0, len(a)): 
    a[i] = int(a[i]) 
a.sort(reverse=True)
sum1=0
sum2=0
for i in range(0, len(a)):
    if(sum1 > sum2):
        sum2 += a[i]
    elif(sum1 & sum2 == 0):
        sum1 += a[i]
    else:
        sum1 += a[i]
if(sum1>sum2):
    print(sum1)
else:
    print(sum2)