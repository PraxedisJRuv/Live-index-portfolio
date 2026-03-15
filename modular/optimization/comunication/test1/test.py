import numpy as np
import mi_modulo

"""
datos = [0]*5

datos[0]=[1,0.5,0,0,0]
datos[1]=[0.5,1,0,0,0]
datos[2]=[0,0,1,0.5,0.5]
datos[3]=[0,0,0.5,1,0]
datos[4]=[0,0,0.5,0,1]

"""
datos=[1,2,3,4,5]
datos=np.array(datos)

# Llamar a la función de C++
resultado = mi_modulo.procesar(datos)

print(resultado)  # Salida: [ 2.  4.  6.  8. 10.]
