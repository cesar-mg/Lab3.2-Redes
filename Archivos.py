import os
f = open('test_100.txt','w')
f.seek(104857600-1) 
f.write('1')
f.close()
print("Se ha generado correctamente el archivo con tamaño: " + str(os.stat('test_100.txt').st_size))

f = open('test_250.txt','w')
f.seek(262144000-1) 
f.write('2')
f.close()
print("Se ha generado correctamente el archivo con tamaño: " + str(os.stat('test_250.txt').st_size))