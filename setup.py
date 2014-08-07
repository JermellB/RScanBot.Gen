from distutils.core import setup
import py2exe
import sys
from glob import glob

datafiles = [("Microsoft.VC90.CRT", glob('C:\Program Files\Microsoft Visual Studio 9.0\VC\redist\x86\Microsoft.VC90.CRT\*.*'))]
sys.path.append("C:\\Program Files\\Microsoft Visual Studio 9.0\\VC\\redist\\x86\\Microsoft.VC90.CRT")
setup(datafiles = datafiles,
      console=['Main.py'],
      options = {"py2exe": {'includes' :  ['htmlentitydefs']}}
      )