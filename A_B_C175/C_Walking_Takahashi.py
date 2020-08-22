
XKD = list(map(int,input().split()))
XKD.sort()
X = XKD[0]
K = XKD[1]
D = XKD[2]

answer = abs(X-(D*0 - D*(K)))
for i in range(K):
    distance = abs(X-(D*i - D*(K-i)))
    if answer >= distance:
        answer = distance
print(answer)
