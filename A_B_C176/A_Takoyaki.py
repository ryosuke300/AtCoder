NXT = list(map(int,input().split()))
NXT.sort()
N = NXT[0]
X = NXT[1]
T = NXT[2]
ans=0
a=N//X
if(N%X==0):
    ans=T*a
else:
    ans=T*(a+1)
print(ans)
