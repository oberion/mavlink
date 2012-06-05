from distutils.core import setup
import py2exe
import os
import sys
parentDir = os.getcwd()
generatorDir = parentDir + '\generator'
sys.path.append(parentDir)
sys.path.append(generatorDir)

setup(console=['generator/mavgen.py'])
