"""

O que é uma estrutura de repetição

-> Serve para executar um bloco de código várias vezes
-> ENQUANTO UMA CONDIÇÃO FOR VERDADEIRA

"""

contador = 0

while contador <= 10:
    contador = contador + 1
   print(contador)

while contador <= 10:
    print(contador)
    contador = contador + 1

# Quero fazer uma contagem de 10 até 0 (decrescente)
contador = 10

while contador >= 0:
    print(contador)
    contador = contador - 1



Qual a lógica de uma tabuada? Quero fazer a tabuada do 5
e deve mostrar

5 x 1 = 5
5 x 2 = 10



#tabuada do 5

Tabuada = 5
contador = 0

while contador <= 10:
    #5 x 1 = 5
    print(tabuada, "x", contador, "=", contador * tabuada)
    contador += 1
