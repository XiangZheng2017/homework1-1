import sys
# Copyright 2017 ZiranLi zrli@bu.edu
for a in sys.argv[1:5]:
   sys.stdout.write(a+"\n")
for b in sys.argv[5:]:
   sys.stderr.write(b+"\n")