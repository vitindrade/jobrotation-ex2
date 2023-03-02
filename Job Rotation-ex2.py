numero = float(input("Qual o número da sequencia de Fibonacci?"))
n1 = 0
n2 = 1 
soma = 1

while (soma < numero):
    soma = n1 + n2
    n1 = n2
    n2 = soma
    print(soma)

if soma == numero:
    print("Este número FAZ parte da Sequencia de Fibonacci")
else:
    print("Este número NÃO faz parte da Sequencia de Fibonacci")

