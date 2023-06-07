class Conta:
    def __init__(self, numero, titular, cpf, saldo, limite):
        self.numero : int = numero
        self.titular : str = titular
        self.cpf : str = cpf
        self.saldo : float = saldo
        self.limite : float = limite

    def __str__(self):
        return f'{self.numero} - {self.titular} - {self.cpf} - {self.saldo} - {self.limite}'