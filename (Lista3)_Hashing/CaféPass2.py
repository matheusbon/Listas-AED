permission = False

def cpf_to_hash(CPF):
    # Inicializa a lista de hash com valores None
    hash_table = [None] * 11

    # Converte o CPF em uma lista de dígitos
    digits = [int(d) for d in str(CPF)]

    # Percorre a lista de dígitos
    for digit in digits:
        # Calcula o índice na tabela hash
        index = digit % 11

        # Se a posição da tabela hash estiver vazia, armazena o valor do dígito multiplicado por 10
        if hash_table[index] is None:
            hash_table[index] = digit * 10
        else:
            # Caso contrário, trata a colisão somando o valor do dígito multiplicado por 10 ao valor já existente
            hash_table[index] += digit * 10

            # Verifica se houve repetição de dígitos
            if len(set(str(hash_table[index]))) < len(str(hash_table[index])):
                # Se houver repetição, calcula a soma dos dígitos repetidos e armazena no primeiro índice
                first_index = str(hash_table[index]).index(str(digit * 10))
                repeated_digits = [int(d) for d in str(hash_table[index])[first_index:]]
                repeated_sum = sum(repeated_digits)
                hash_table[first_index] = repeated_sum
    hash_table = [d for d in hash_table if d is not None]
    return hash_table



def check_permission(hash_table, magic_number):
    table = []
    
    for digit in hash_table:
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

    hash_table = cpf_to_hash(CPF)
    permission = check_permission(hash_table, magic_number)
    
    if permission:
        print("UP Permission")
    
    else:
        print("NOT Permission")
