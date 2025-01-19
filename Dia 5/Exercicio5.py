"""Escreva um programa que crie a Tabuada."""

def gerar_tabuada(numero):
    print("Tabuada do {numero}")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} X {i} = {resultado}")

numero = int(input("Digite o numero para gerar a Tabuada:"))

gerar_tabuada(numero)