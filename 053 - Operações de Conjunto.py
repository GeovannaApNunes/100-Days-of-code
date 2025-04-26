# Definição dos conjuntos
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# União (elementos que estão em A ou B)
uniao = A | B  # ou A.union(B)

# Interseção (elementos que estão em A e B)
intersecao = A & B  # ou A.intersection(B)

# Diferença (elementos que estão em A, mas não em B)
diferenca_A_B = A - B  # ou A.difference(B)
diferenca_B_A = B - A  # ou B.difference(A)

# Diferença simétrica (elementos que estão em A ou B, mas não em ambos)
diferenca_simetrica = A ^ B  # ou A.symmetric_difference(B)

# Verificação de subconjunto (A é subconjunto de B?)
subconjunto = A <= B  # ou A.issubset(B)

# Verificação de superconjunto (A contém todos os elementos de B?)
superconjunto = A >= B  # ou A.issuperset(B)

# Exibição dos resultados
print(f"União: {uniao}")
print(f"Interseção: {intersecao}")
print(f"Diferença A - B: {diferenca_A_B}")
print(f"Diferença B - A: {diferenca_B_A}")
print(f"Diferença Simétrica: {diferenca_simetrica}")
print(f"A é subconjunto de B? {subconjunto}")
print(f"A é superconjunto de B? {superconjunto}")
