class MyOpen:
    def __init__(self, caminho_arquivo, mode):
        self.caminho_arquivo = caminho_arquivo
        self.mode = mode
        
    def __enter__(self):
        print("Abrindo arquivo")
        self._arquivo = open(self.caminho_arquivo, self.mode, encoding='utf-8')
        return self._arquivo
    def __exit__(self, class_exception, exception_, traceback_):
        print("Fechando arquivo")
        self._arquivo.close()
        
instancia = MyOpen('aula240.txt', 'w')

with instancia as arquivo:
    arquivo.write('Teste!')
    print('WITH', arquivo)
