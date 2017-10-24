import os
import sys
import re

path = os.path.abspath(os.path.dirname(sys.argv[0]))

inputs = open(path+'/test/inputs.txt', 'r', encoding='ISO-8859-1')
outputs = open(path+'/test/outputs.txt', 'w', encoding='ISO-8859-1')

for s in inputs.readlines():
    outputs.write(s.replace('\n','abc'))

inputs.close()
outputs.close()