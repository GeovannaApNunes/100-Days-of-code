class Carro:
    """Classe que representa um carro simples."""
    
    def __init__(self, marca, modelo):
        """Inicializa um carro com marca e modelo."""
        self.marca = marca
        self.modelo = modelo
        self.ligado = False  # O carro começa desligado

    def start(self):
        """Liga o carro."""
        if not self.ligado:
            self.ligado = True
            print(f"O {self.marca} {self.modelo} foi ligado.")
        else:
            print(f"O {self.marca} {self.modelo} já está ligado.")

    def stop(self):
        """Desliga o carro."""
        if self.ligado:
            self.ligado = False
            print(f"O {self.marca} {self.modelo} foi desligado.")
        else:
            print(f"O {self.marca} {self.modelo} já está desligado.")

# Testando a classe Carro
meu_carro = Carro("Opala", "67")
meu_carro.start()  # Liga o carro
meu_carro.start()  # Tenta ligar novamente
meu_carro.stop()   # Desliga o carro
meu_carro.stop()   # Tenta desligar novamente