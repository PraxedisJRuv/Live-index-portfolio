from setuptools import setup, Extension
import pybind11

ext_modules=[
    Extension(
        "kmedoids",
        ["kmedoids.cpp"],
        include_dirs=[pybind11.get_include()],
        language="c++"
    )
]

setup(
    name="kmedoids_cpp",
    ext_modules=ext_modules,
)