"""Função de soma"""
def soma(a, b):
    resultado = a + b
    print(f"Resultado da função de soma é igual a: {resultado}")
    return resultado

"""Input de número"""
a= int(input("Digite o primeiro número a ser somado: "))
b= int(input("Digite o segundo número a ser somado: "))

"""Variável de soma"""
resultado= soma(a,b)

"Outra variável de soma usando return"
resultadofinal= resultado + 2
print(f"Resultado final é igual a= {resultadofinal}")