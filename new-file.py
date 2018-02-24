#Este es el ejercicio del caso practico 05 realizado en clase

import glob
import re

file_in=open('tabla1.csv','r')

isfirstline = True
n=0

for line in file_in:
    if isfirstline:
        isfirstline = False
        continue
    text = line.split('.')
    #clave o  filename
    clave = texto[0]+'-'+text[1]+text[6]+'.txt'
    print(clave)
    f = open(clave, 'a')
    clave.write(text[-1])

    f.close()

    n+=1

    if n== 5000:
        break

file_in.close()
