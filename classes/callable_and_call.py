class CallMe:
    def __init__(self, phone):
        self.phone = phone
    
    def __call__(self, nome):
        print(f'Chamando {nome} pelo telefone {self.phone}')
        
call1 = CallMe('123-456')
call1('Lucas')        
