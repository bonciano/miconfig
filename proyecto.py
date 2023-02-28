import os

#def pregunta(paquete):
#    p = input(f'Instalar {paquete}? y/n:')
#    if p == 'y':
#        cmd = f'source venv/bin/activate;pip install {paquete}'
#        os.system(cmd)
#        os.system('deactivate')
#        return f'{p} se instalo correctamente..'
#    else:
#        return f'{p} no fue instalado..'



nombre = input('Nombre del proyecto: ')

os.system('clear')

print(f'Inicio de la creacion del proyecto {nombre}')
print('------------------------ O ------------------------')

cmd = f'mkdir {nombre};cd {nombre};git init;virtualenv venv;'
os.system(cmd)

#paquetes = input('Desea instalar paquetes? y/n: ')
#
#if paquetes == 'y':
#    pregunta('django')

print(f'Fin de la creacion del proyecto {nombre}')
print('------------------------ O ------------------------')






# Fin del programa
