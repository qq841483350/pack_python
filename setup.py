#coding:utf8
from distutils.core import setup
import py2exe
setup(console=["weiyuanchuang.py"])
#setup(windows=["weiyuanchuang.py"],options = { "py2exe":{"dll_excludes":["MSVCP90.dll"]}})  #编译为WINDOWS  GUI程序

