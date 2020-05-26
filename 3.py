#! /usr/local/bin/python

import sys

line1, line2 = map(lambda line: line.rstrip(), sys.stdin)

dirs = {
  "R":(0,1),
  "L":(0,-1),
  "U":(1,0),
  "D":(-1,0)
}

seen = {}
curx,cury = 10000, 10000
steps = 0
for ins in line1.split(","):
  dx, dy = dirs[ins[0]]
  length = int(ins[1:])
  for s in xrange(0, length):
    steps += 1
    curx, cury = curx + dx, cury + dy
    if (curx, cury) not in seen:
      seen[(curx, cury)] = steps
    
curx,cury = 10000, 10000
steps = 0
for ins in line2.split(","):
  dx, dy = dirs[ins[0]]
  length = int(ins[1:])
  for s in xrange(0, length):
    steps += 1
    curx, cury = curx + dx, cury + dy
    if (curx, cury) in seen:
      print curx, cury
      print steps + seen[curx, cury]
