matriz = [[False for i in range(501)] for j in range(501)]
n = int(input())
l = 0
for k in range(n):
    x,y = map(int, input().split())
    if matriz[x][y]:
        l = 1
    else:
        matriz[x][y] = True
print(l)