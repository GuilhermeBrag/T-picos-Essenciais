import os
os.system('cls')
 
#Funções
def calc_resistencia(re1, re2, re3, re4):
    resistencia = re1 + re2 + re3 + re4
    return resistencia
 
 
 
print("********* EXERCICIO 02 *********")
re1 = int(input("Digite o valor da primeira resistência: "))
re2 = int(input("Digite o valor da segunda resistência: "))
re3 = int(input("Digite o valor da terceira resistência: "))
re4 = int(input("Digite o valor da quarta resistência: "))
 
print("\n ********* RESULTADO *********")
resultado_final = calc_resistencia(re1, re2, re3, re4)
print("O resultado total da resistência do circuito é: ", resultado_final)
print(f"Resistencias fornecidadas: {re1},{re2},{re3},{re4}",)
print(f"A maior resistência é: {max(re1, re2, re3, re4)}")



print("\n\n\n")
