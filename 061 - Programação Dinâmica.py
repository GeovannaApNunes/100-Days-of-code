def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

# Exemplo de uso
for i in range(11):
    print(f"Fibonacci({i}) = {fibonacci(i)}")
