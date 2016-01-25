#!/usr/bin/python

import os, sys
#from datetime import date

print "Backup to Server."
print
print "Does not push tags."

#today = date.today()

gitadd = r'git add .'
gitcommit = r'git commit -a -m'+' "'+'regular commit'+'"'
gitpushall = r'git push --all origin'
gitpushtags = r'git push --tags origin'

print gitadd
print gitcommit
print gitpushall
print gitpushtags

print
print "Collecting information..."
os.system(gitadd)
print
print "Committing changes..."
os.system(gitcommit)
print
print "Uploading changes..."
if os.system(gitpushall) == 0 :
 if os.system(gitpushtags) == 0: 
  print "Upload success!"
  print
  print
  raw_input("Press Enter to finish")
  sys.exit(0)
  
print "*******************"
print "Upload failed!!"
print
print
raw_input("Press Enter to finish")


  
