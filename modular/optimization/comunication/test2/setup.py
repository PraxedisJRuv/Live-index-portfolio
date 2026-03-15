import numpy as np
import miprocesador

A = np.array([
    [1.0,2.0,3.0],
    [4.0,5.0,6.0]
])

B = miprocesador.procesar(A)

print(B)