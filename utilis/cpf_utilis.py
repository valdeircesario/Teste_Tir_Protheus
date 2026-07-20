import random

def gerar_cpf(formatado=False):
    cpf = [random.randint(0, 9) for _ in range(9)]

    # Primeiro dígito
    soma = sum((10 - i) * cpf[i] for i in range(9))
    d1 = (soma * 10 % 11) % 10
    cpf.append(d1)

    # Segundo dígito
    soma = sum((11 - i) * cpf[i] for i in range(10))
    d2 = (soma * 10 % 11) % 10
    cpf.append(d2)

    cpf_str = ''.join(map(str, cpf))

    if formatado:
        return f"{cpf_str[:3]}.{cpf_str[3:6]}.{cpf_str[6:9]}-{cpf_str[9:]}"
    
    return cpf_str