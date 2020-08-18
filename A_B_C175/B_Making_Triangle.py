#一つ目の入力で個数を決める
N=int(input())
#入力されたLの値をそれぞれ区切ってlistのlに格納
l= list(map(int,input().split()))
l.sort()
#満たすものがない時0を出力
answer =0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            #3つの整数は1<=i<=j<=k<=N
            a = l[i]
            b = l[j]
            c = l[k]
            #3つの整数はすべて異なる
            if a==b or b==c or c==a:
                continue
            if l[i]+l[j] >　l[k]:
                answer +=1
print(answer)
