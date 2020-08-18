N=int(input())

count1=0
count2=0
count3=0
count4=0
for i in range(N):
    S = input()
    if S=="AC":
        count1+=1
    if S=="WA":
        count2+=1
    if S=="TLE":
        count3+=1
    if S=="RE":
        count4+=1

print("AW × ",count1)
print("WA × ",count2)
print("TLE × ",count3)
print("RE × ",count4)
