def Fibonacci(num): 
    
    if num < 0: 
        return False 
    
    a, b = 0, 1
    while a <= num:
        if a == num:
            return True 
        a, b = b, a + b
    return False 

try:
    numero = int(input('Digite um número'))
    if Fibonacci(numero):
        print(f'O número {numero}  pertence a sequencia de Fibonacci') 
    else:
        print(f'O número {numero} não pertence a sequencia de Fibonacci')   
except ValueError:
    print('inválido! tente denovo.')
  


