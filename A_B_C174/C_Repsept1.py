#解答例
K = int(input())
#Kが7で割り切れるか見る
a = 7%K
ans = -1
for i in range(1,10**6+1):
    #割り切れたものに対して
  if a==0:
    ans = i
    break
  a = (a*10+7)%K
print(ans)
