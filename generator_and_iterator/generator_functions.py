def generator(n=0, maximum=10):
   while True:
    yield n
    n += 1
    if n > maximum:
        return print('STOP GENERATOR')


gen = generator(maximum=800)
for n in gen:
    print(n)
