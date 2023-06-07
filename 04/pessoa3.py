class Pessoa3:
    def __init__(self, nome, sobrenome, peso, idade) :
        self.Sobrenome : str = sobrenome
        self.Peso : float = peso 
        self.Nome : str = nome
        self.Idade : int = idade
    
        
    def __str__(self) :
        return f'{self.Nome} {self.Sobrenome} {self.Peso} {self.Idade}'