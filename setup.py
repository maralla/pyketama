from setuptools import setup
from setuptools.extension import Extension
from Cython.Distutils import build_ext


ext_modules = [
    Extension("ketama.ketama", ["contrib/md5.c", "contrib/ketama.c",
                                "ketama/ketama.pyx"],
              include_dirs=["contrib"])
]

setup(name="pyketama",
      license="MIT",
      zip_safe=False,
      cmdclass={"build_ext": build_ext},
      ext_modules=ext_modules
      )
