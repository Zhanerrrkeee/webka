n = int(input())
a = list(map(int, input().split()))
cnt = 0
for i in range(0,n-1):
    if a[i]>0 and a[i+1]>0:
        cnt+=1
    elif a[i]<0 and a[i+1]<0:
        cnt+=1
if cnt==0:
    print("NO")
else:
    print("YES")
