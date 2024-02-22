def verify(num):
    a, b = 0, 1
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b
    return False

input_num = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

if verify(input_num):
    print(f"O número {input_num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {input_num} não pertence à sequência de Fibonacci.")