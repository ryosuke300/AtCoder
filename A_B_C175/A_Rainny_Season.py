
S = input()
a=0
for i in range(3):
    if a==0:
        if S[i]=="R":
            a+=1
    else:
    #連続している数を以下のように判断
        if S[i-1]=="R" and S[i]=="R":
            a+=1
print(a)
