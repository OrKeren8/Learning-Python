from typing import Optional


def opt_func(var: Optional[str] = None):
    print(type(var))

def py_3_10(var: str | None):
    print(type(var))

opt_func('i')
opt_func()
py_3_10('i')
py_3_10(None)

"""
as from this example we can see that optional fives the aportunity 
to set the var or not, eather way it will be fune

in python 3.10 the | operator determine the different types of data i could get in a function
"""


































