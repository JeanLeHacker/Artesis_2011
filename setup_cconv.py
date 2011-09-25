#!/usr/bin/env python 
""" 
setup.py file for SWIG cconv
""" 
from distutils.core import setup, Extension 

cconv_module = Extension('_cconv', 
                  include_dirs = ["/opt/local/include"],
                  sources=['cconv_wrap.c', 'cconv.c'], 
                  define_macros=[],
                  extra_compile_args=[('-DSIMULATOR'),] 
                ) 
setup (name        = 'cconv', 
       version     = '0.1', 
       author      = "Jan Mennekens", 
       description = """cconv support routines""", 
       ext_modules = [cconv_module], 
       py_modules = ["cconv"], 
       ) 

