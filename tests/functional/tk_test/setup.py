from distutils.core import setup
import py2exe

setup(console=[{ "script": "tk_test.py"}],
      options={"py2exe": {"packages": ['tkinter']}
              }
     )