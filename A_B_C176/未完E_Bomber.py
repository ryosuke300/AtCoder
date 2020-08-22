import random
H,W,M = map(int,input().split())
xy = [map(int, input().split()) for _ in range(M)]
x, y = [list(i) for i in zip(*xy)]


X2 =[list random.randint() for _ in range(M)]
y2 =[list random.randint() for _ in range(M)]
