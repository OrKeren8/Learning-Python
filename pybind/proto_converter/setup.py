from setuptools import setup, Extension
import pybind11

ext_modules = [
    Extension(
        "Converter",
        ["converter.cpp"],
        include_dirs=[pybind11.get_include()],
        language="c++"
    ),
]

setup(
    name="Converter",
    ext_modules=ext_modules,
)
