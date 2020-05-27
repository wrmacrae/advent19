#! /usr/local/bin/python

import sys

bounds = sys.stdin.readline().strip()
minVal, maxVal = bounds.split("-")
minVal, maxVal = int(minVal), int(maxVal)

def adjacent(candidate):
  for i in xrange(5):
    if str(candidate)[i] == str(candidate)[i+1]:
      return True
  return False

def increasing(candidate):
  for i in xrange(5):
    if int(str(candidate)[i]) > int(str(candidate)[i+1]):
      return False
  return True

def double(candidate):
  i = 0
  while i < 5:
    runlen = 1
    for j in xrange(i+1,6):
      if candidate[i] == candidate[j]:
        runlen += 1
      else:
        break
    if runlen == 2:
      return True
    i=j
  return False
    
  for i in xrange(5):
    if str(candidate)[i] == str(candidate)[i+1]:
      return True
  return False

count = 0
for candidate in xrange(minVal, maxVal+1):
  if increasing(candidate) and double(str(candidate)):
    count += 1
print count
