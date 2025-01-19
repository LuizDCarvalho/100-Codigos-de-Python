"""Convertendo temperatura de Celsius para Fahrenheit"""

def converter(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

entrada = float(input("Digite a temperatura em celsius:"))

print(f"Sua temperatura em fahrenheit é: {converter(entrada)}")