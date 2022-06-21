valor = int(input('Informe um valor inteiro para conferir se ele pertence a sequência fibonacci: '))

fib, a, b= 0, 0, 1

while valor > fib:
    fib = a+b   
    a, b = b, fib    
if valor == fib:
    print('\nValor pertence a sequência fibonacci')
else:
    print('\nValor não pertence a sequência fibonacci')