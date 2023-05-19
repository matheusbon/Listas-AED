permission = False

def check_repeated(CPF):
    digits = [(int(digit) * 10) for digit in CPF]
    hash_table = [[] for i in range(11)]   
    support = []
    digits_final = []
    
    for i, digit in enumerate(digits):
        # Verifica se o dígito já foi encontrado anteriormente
        if digit // 10 in support:
            total = None
        else:
            # Se não foi encontrado, calcula a soma (total) e adiciona na table hash e também adiciona o número do cpf na lista auxiliar (para sinalizar que ele e suas repetições já foram tratadas)
            total = sum(int(d) for d in digits if d == digit)
            hash_table[digit // 10] = total
            support.append(digit // 10)

        digits_final.append (total)

    # Remove os valores "None" da lista
    digits_final = [d for d in digits_final if d is not None]

    return(digits_final)


def check_permission(digits_final, magic_number):
    table = []
    
    for digit in digits_final:
        if digit in table:
            permission = True
            break
        else:
            complemento = magic_number - digit
            table.append(complemento)
            permission = False

    return (permission)

num_entradas = int(input())
for i in range (num_entradas):
    entrada = input()
    CPF, magic_number = entrada.split()
    magic_number = int(magic_number)

    digits_final = check_repeated(CPF)
    permission = check_permission(digits_final, magic_number)
    
    if permission:
        print("UP Permission")
    
    else:
        print("NOT Permission")
