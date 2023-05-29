letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra)
    
    if 'j' in letras:
        print('Muito bem! Esse é o fim!')
        break
    
    print(letras)
    