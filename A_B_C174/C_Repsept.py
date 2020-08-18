
K = int(input())


a = 7
for i in range(1,10**6+1):
    if a%K ==0:
        break
    else:
        a += (10**i)*7

print(len(str(a)))
