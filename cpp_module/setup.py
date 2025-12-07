from skbuild import setup
from setuptools import Extension
import pybind11

setup(
    name="my_atom",
    version="0.1",
    ext_modules=[
        Extension(
            "my_atom",
            ["bindings.cpp"],
            include_dirs=[pybind11.get_include()],
            language="c++"
        )
    ],
)

