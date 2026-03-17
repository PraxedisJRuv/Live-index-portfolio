from setuptools import setup, Extension
import pybind11

ext_modules=[
    Extension(
        "miprocesador",
        ["procesador.cpp"],
        include_dirs=[pybind11.get_include()],
        language="c++"
    )
]

setup(
    name="miprocesador",
    ext_modules=ext_modules,
)
"""
La clase Extension define un módulo de extensión con
nombre "miprocesador", junto las referencias para
hallar el archivo de c++
el get include es para que los encabezados se incluyan
al momento de compilar el código de c++

Veamos si funciona
python setup.py build
Esto para la configuración
Se generó correctamente

python setup.py install
Esto para compilar
"""