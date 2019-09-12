nt = 0
n = int(input())
while n != 0:
    nt = nt + 1
    nome_par = input()
    nome_ímpar = input()
    print("Teste ", nt)
    for i in range(n):
        a, c = map(int, input().split())
        if (a + c) % 2 == 0:
            print(nome_par)
        else:
            print(nome_ímpar)
    print()
    n = int(input())