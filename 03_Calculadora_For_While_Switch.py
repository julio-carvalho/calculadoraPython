from io import open_code

def tabuada (var):
    for i in range(11):
        print(f"{var} x {i} = {var*i}")

def calculo (op, num1, num2):
    match op:
        case (1):
            resultado = num1 + num2
            print(f"\n{num1} + {num2} = {resultado}")
        case (2):
            resultado = num1 - num2
            print(f"\n{num1} - {num2} = {resultado}")
        case (3):
            resultado = num1 * num2
            print(f"\n{num1} x {num2} = {resultado}")
        case (4):
            resultado = num1 / num2
            print(f"\n{num1} : {num2} = {resultado}")
        case (5):
            resultado = num1 % num2
            print(f"\n{num1} : {num2} = {resultado}")
        ## case _:
        ##    print("Opção inválida")


num1 = 0
num2 = 0
resultado = 0
sair = 1

while sair == 1:

    op = (int(input("Digite o número da operação: \n1 - Adição \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n5 - Quoeficiente\n6 - Tabuada\n")))
    
    if (op == 6):
        num1 = (float(input("Digite o número para a tabuada: ")))
        tabuada(num1)
    elif (op >= 1 and op <= 5):
        num1 = (float(input("\nDigite primeiro número: ")))
        num2 = (float(input("Digite o segundo número: ")))
        calculo(op, num1, num2)
    else:
        print("Opção inválida!")


    sair = (int(input("\nDeseja continuar?\n1 - Sim \n2 - Não\n")))

print("\nPrograma finalizado!")
    
