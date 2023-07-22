N = int(input('Quantidade de casos de teste: '))
n = N

while(n > 0):
    A = input('Valor A: ')
    B = input('Valor B: ')
    contB = len(B)
    listA = A
    listB = B
    listaInv = listA[::-1]
    listaInv = listaInv[0:contB]
    listaRev = listaInv[::-1]
    if listaRev == listB:
        print('encaixa')
    else:
        print('nao encaixa')

    n -= 1
'''
print(contB)
listaInv = listA[::-1]
print(listaInv)
print(listaInv[0:contB])
listaRev = listaInv[::-1]
'''
