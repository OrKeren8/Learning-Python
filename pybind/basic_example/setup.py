# setup.py
from setuptools import setup, Extension
import pybind11

ext_modules = [
    Extension(
        "heavyCalc",
        ["heavyCalc.cpp"],
        include_dirs=[pybind11.get_include()],
        language="c++"
    ),
]

setup(
    name="heavyCalc",
    ext_modules=ext_modules,
)
