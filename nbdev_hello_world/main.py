"""This is the second alteration of the notebook"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_main.ipynb.

# %% auto 0
__all__ = ['main', 'say_hello', 'square', 'User']

# %% ../nbs/00_main.ipynb 3
def main(): return 1 + 1

# %% ../nbs/00_main.ipynb 4
def say_hello(to): 
    "Say hello to somebody"
    return f"Hello {to}!"

# %% ../nbs/00_main.ipynb 6
def square(x):
    "Square the number x"
    return x*x

# %% ../nbs/00_main.ipynb 7
from dataclasses import dataclass

# %% ../nbs/00_main.ipynb 8
@dataclass
class User:
    name: str
    age: int
    administrator: bool
    def to_json(self):
        return f'{{"class": "User", "age": {self.age}, "name": {self.name}, "administrator": {self.administrator} }}'
