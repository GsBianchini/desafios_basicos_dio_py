#DESAFIO: Paulinho tem em suas mãos um novo problema. Agora a sua professora lhe pediu que construísse um programa para verificar, à partir de dois valores muito grandes A e B, se B corresponde aos últimos dígitos de A.
#A entrada consiste de vários casos de teste. A primeira linha de entrada contém um inteiro N que indica a quantidade de casos de teste. Cada caso de teste consiste de dois valores A e B maiores que zero, cada um deles podendo ter até 1000 dígitos.
#Para cada caso de entrada imprima uma mensagem indicando se o segundo valor encaixa no primeiro valor, confome exemplo abaixo.

def verifica_encaixe(A, B):
    if len(B) > len(A):
        return False
    if A[-len(B):] == B:
        return True
    else:
        return False

# Lê a quantidade de casos de teste
N = int(input())

# Realiza a verificação para cada caso de teste
for _ in range(N):
    A, B = input().split()
    if verifica_encaixe(A, B):
        print("encaixa")
    else:
        print("nao encaixa")