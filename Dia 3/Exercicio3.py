def adicao(x, y):  # Corrigi o cabeçalho da função
    return x + y

def subtracao(x, y):  # Corrigi o cabeçalho da função
    return x - y

def multiplicacao(x, y):  # Corrigi o cabeçalho da função
    return x * y

def divisao(x, y):  # Corrigi o cabeçalho da função
    return x / y

def calculadora():
    print("Selecione a Operacao desejada.")
    print("1 - soma")
    print("2 - subtracao")
    print("3 - multiplicacao")
    print("4 - divisao")
    
    while True:
        escolha = input("Escolha(1/2/3/4): ")
        
        if escolha in ('1', '2', '3', '4'):
            x = int(input("Digite o primeiro numero: "))
            y = int(input("Digite o segundo numero: "))
        
        if escolha == '1':
            print("Resultado: ", adicao(x, y))
        if escolha == '2':
            print("Resultado: ", subtracao(x, y))
        if escolha == '3':
            print("Resultado: ", multiplicacao(x, y))
        if escolha == '4':
            if y != 0:
                print("Resultado: ", divisao(x, y))
            else:
                print("Nao pode ser dividido por zero")
        else:  # Corrigi a lógica do else
            print("Escolha invalida")
        
        continuar = input("Quer Fazer outra Operacao? (s/n): ")  # Corrigi a captura de input
        if continuar == 'n':
            print("Obrigado")
            break

# Executando a função principal
calculadora()
