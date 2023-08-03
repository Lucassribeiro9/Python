import importlib
import mod_teste

for i in range(10):
    importlib.reload(mod_teste)
print('end') 