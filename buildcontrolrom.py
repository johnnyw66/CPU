
#!/bin/env python
import os
from setuptools import setup, find_packages
from glob import glob
import sys
from objutils import Image, Section, dump, dumps, load, loads

print("building control rom...") ;
sec0 = Section(start_address = 0x1000, data = "Hello HEX world!")
#sec0.hexdump()

sec1 = Section(0x2000, range(1, 17))
#sec1.hexdump()

img0 = Image([sec0, sec1])
print(img0)

dump("srec", "example0.srec", img0)
dump("ihex", "example0.hex", img0)
