#Projeto (Cálculo Simples) -> https://github.com/jeanhackerdobem
#Autor: Jean Marcelo -> https://linkedin.com/in/jmdba
#Contatos: https://instagram.com/jean.marcelo.1

num1 = int(input("***Calculadora Simples***\nDigite um número e aperte a tecla ENTER!\n-> "))

action = str(input("Selecione um dos cálculos matemáticos abaixo, e aperte a tecla ENTER:\n\nAdição(+)\n\nSubtração(-)\n\nMultiplicação(*)\n\nDivisão(/)\n-> "))

num2 = int(input("Digite mais um número e aperte a tecla ENTER!\n-> "))

print("Resultado: ")

if action == "+":
    print(num1+num2)
elif action == "-":
    print(num1-num2)
elif action == "*":
    print(num1*num2)
else:
    print(num1/num2)
