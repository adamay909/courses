#!/usr/bin/python

import os

print "Pull from Server."
print


gitadd = r'git add .'
gitcommit = r'git commit -a -m'+' "regular commit"'
gitpush = r'git push --all --tags origin'
gitpull = r'git pull'

if os.system(gitpull) == 0:
  print "Pull success!"
  print
  print
  raw_input("Press Enter to finish")
else:
  print "*******************"
  print "Pull failed!!"
  print
  print
  raw_input("Press Enter to finish")


  
