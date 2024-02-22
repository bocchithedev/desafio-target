def inverter(string):
    caracteres = list(string)
    
    tamanho = len(caracteres)
    
    for i in range(tamanho // 2):
        caracteres[i], caracteres[tamanho - i - 1] = caracteres[tamanho - i - 1], caracteres[i]
    
    return ''.join(caracteres)

string = input("Qual o seu nome?: ")

string_invertida = inverter(string)

print(string_invertida , "álO")