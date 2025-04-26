def torre_de_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mova o disco 1 de {origem} para {destino}")
        return
    torre_de_hanoi(n-1, origem, auxiliar, destino)
    print(f"Mova o disco {n} de {origem} para {destino}")
    torre_de_hanoi(n-1, auxiliar, destino, origem)

# Pegando input do usuário
try:
    n = int(input("Digite o número de discos: "))
    print(f"\nSolução para {n} discos:\n")
    torre_de_hanoi(n, 'A', 'C', 'B')
except ValueError:
    print("Por favor, digite um número inteiro válido.")
