class Foo:
    def __init__(self):
        self.public = 'public'
        self._protected = 'protected'
        self.__private = 'private'

    def metodo_publico(self):
        print(self.__private)
        self.__metodo_privado()
        return 'metodo_publico'
    def _metodo_protegido(self):
      print('_metodo_protegido')
      return '_metodo_protegido'  
    def __metodo_privado(self):
      print('__metodo_privado')
      return '__metodo_privado'
  
foo = Foo()
print(foo.metodo_publico())