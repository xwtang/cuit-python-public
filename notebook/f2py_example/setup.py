from numpy.distutils.core import setup as f2py_setup
from numpy.distutils.core import Extension as f2py_Extension


# f2py modules
f2py_ext = [
    f2py_Extension(
        'flib',
        sources=['flib.f90'])
]
f2py_setup(ext_modules=f2py_ext)
