import os
os.system('cls')


nomeProd = str(input("Digite o nome do produto: "))
valorProd = float(input("Digite o valor do produto: "))


if valorProd >= 50 and valorProd < 200:
    res = valorProd - (valorProd * 0.05) 
elif valorProd >= 200 and valorProd < 500:
     res = valorProd - (valorProd * 0.06)  
elif valorProd >= 500 and valorProd < 1000:
     res = valorProd -(valorProd * 0.07)
elif valorProd >= 1000:
     res = valorProd - (valorProd * 0.08)         
else:
     print("Nenhum desconto!")
print (nomeProd)
print (valorProd)
print(res)
