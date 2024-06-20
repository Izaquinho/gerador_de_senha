import random

def gerar_senha():
    # Gera uma sequência específica para A, B, C (em maiúsculas ou minúsculas)
    letras = ''.join([
        random.choice(['a', 'A']),
        random.choice(['b', 'B']),
        random.choice(['c', 'C'])
    ])
    
    # Conjunto de caracteres especiais permitidos
    caracteres_especiais = "!#*.?@_"
    
    # Escolhe dois caracteres especiais aleatórios
    caracteres = ''.join(random.choice(caracteres_especiais) for _ in range(2))
    
    # Gera dias e meses no formato DDMM
    dia = f"{random.randint(1, 31):02d}"
    mes = f"{random.randint(1, 12):02d}"
    data = dia + mes

    # Combina todas as partes para formar a senha
    senha = letras + caracteres + data

    return senha

def main():
    while True:
        senha_gerada = gerar_senha()
        print("Senha gerada:", senha_gerada)
        
        resposta = input("Deseja gerar outra senha? (s/n): ").strip().lower()
        if resposta != 's':
            break

if __name__ == "__main__":
    main()
