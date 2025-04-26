# Definição das classes de exceção personalizadas
class ErroPersonalizado(Exception):
    """Exceção base para erros personalizados."""
    pass

class ValorMuitoBaixoErro(ErroPersonalizado):
    """Exceção para valores muito baixos."""
    def _init_(self, valor, mensagem="O valor fornecido é muito baixo!"):
        self.valor = valor
        self.mensagem = mensagem
        super()._init_(f"{mensagem} Valor recebido: {valor}")

class ValorMuitoAltoErro(ErroPersonalizado):
    """Exceção para valores muito altos."""
    def _init_(self, valor, mensagem="O valor fornecido é muito alto!"):
        self.valor = valor
        self.mensagem = mensagem
        super()._init_(f"{mensagem} Valor recebido: {valor}")

# Função de teste que lança exceções personalizadas
def verificar_valor(valor):
    if valor < 10:
        raise ValorMuitoBaixoErro(valor)
    elif valor > 100:
        raise ValorMuitoAltoErro(valor)
    else:
        print(f"Valor {valor} está dentro do intervalo permitido.")

# Testando as exceções
try:
    valor_teste = int(input("Digite um valor: "))
    verificar_valor(valor_teste)
except ValorMuitoBaixoErro as e:
    print(f"Erro: {e}")
except ValorMuitoAltoErro as e:
    print(f"Erro: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")