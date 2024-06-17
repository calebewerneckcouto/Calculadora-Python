def numerosdividir(n1,n2):
    resultado = n1/n2
    return print(f'A divisão do valor {n1} e {n2} e igual a {resultado}')

def numerosmultiplicar(n1,n2):
     resultado = n1*n2
     return print(f'A Multiplicação do valor {n1} e {n2} e igual a {resultado}')

def numerossomar(n1,n2):
     resultado = n1+n2
     return print(f'A Soma do valor {n1} por {n2} e igual a {resultado}')


opcao = 0

def numerossubtrair(n1,n2):
     resultado = n1/n2
     return print(f'A divisão do valor {n1} por {n2} e igual a {resultado}')
def menu(opcao):
    if(opcao == '1'):
        n1= int(input('Informe o primeiro valor:'))
        n2= int(input('Informe o segundo valor :'))
        return numerossomar(n1,n2)
    elif(opcao == '2'):
        n1= int(input('Informe o primeiro valor:'))
        n2= int(input('Informe o segundo valor :'))
        return numerossubtrair(n1,n2)
    elif(opcao == '3'):
        n1= int(input('Informe o primeiro valor:'))
        n2= int(input('Informe o segundo valor :'))
        return numerosmultiplicar(n1,n2)
    elif(opcao == '4'):
        n1= int(input('Informe o primeiro valor:'))
        n2= int(input('Informe o segundo valor :')) 
        return numerosdividir(n1,n2)
   

   

print("-------- Calculadora ---------------")
print(' 1 - soma ')
print(' 2 - subtracao ')
print(' 3 - Multiplicação ')
print(' 4 - Divisao ')
print(' 5 - Sair ')

opcao = input('Informe uma Opção: ')
menu(opcao)
    
   
