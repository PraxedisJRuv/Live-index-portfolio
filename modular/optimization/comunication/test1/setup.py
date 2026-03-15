from setuptools import setup, Extension
import pybind11

# Definición del módulo
ext_modules = [
    Extension(
        'mi_modulo',
        ['main.cpp'], # Tu archivo C++
        include_dirs=[pybind11.get_include()],
        language='c++'
    ),
]

setup(
    name='mi_modulo',
    ext_modules=ext_modules,
)
