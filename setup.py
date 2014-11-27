# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages
from setuptools.extension import Extension


try:
    from Cython.Distutils import build_ext
    cmdclass = {"build_ext": build_ext}
except ImportError:
    if os.path.exists("ketama/ketama.c"):
        ext = Extension("ketama.ketama", ["contrib/md5.c", "contrib/ketama.c",
                                          "ketama/ketama.c"],
                        include_dirs=["contrib"])
        cmdclass = {}
    else:
        print("Fatal: Cython is required to compile pyketama")
        exit(1)


ext = Extension("ketama.ketama", ["contrib/md5.c", "contrib/ketama.c",
                                  "ketama/ketama.pyx"],
                include_dirs=["contrib"])

setup(
    name="pyketama",
    version="0.2.0",
    author="maralla",
    author_email="maralla.ai@gmail.com",
    url="https://github.com/maralla/pyketama",
    description="ketama consistent hashing in cython",
    long_description=open("README.md").read(),
    keywords="python ketama consistent hash cython",
    packages=find_packages(),
    license="BSD",
    zip_safe=False,
    cmdclass=cmdclass,
    ext_modules=[ext],
    classifiers=[
        "Topic :: Software Development",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ]
)
