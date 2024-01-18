class MinhaClasse:
    def __new__(cls, *args, **kwargs):
        print("Chamando o método __new__")
        instance = super().__new__(cls)
        return instance

    def __init__(self, *args, **kwargs):
        print("Chamando o método __init__")
        self.valor = 0

objeto = MinhaClasse()