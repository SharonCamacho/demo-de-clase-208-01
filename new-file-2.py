#Ejercicio caso practico 05 parte 2

import glob
import re
import os

file_out=open('tabla2.csv','w')
file_out.write('ESTACIÓN, ANO, MES, DIA, HORA,VEL\n')

for clave in glob.glob('*.txt'):
    file_in = open(clave, 'r')

    lines= file_in.readlines()
    text= [float(x) for x in lines]
    clave = clave.replace('-',',')
    prom  = sum(text)/len(text)
    prom = '%5.2f' % prom
    file_out.write(clave[:-4]+'-'+str(prom)+'\n')
    fine_in.close()

    n += 1

    if n == 10:
        break
file_out.close()
os.remove('*.txt')
