#!/bin/bash

#for line in `cat 1.txt`; do
#  expr $line / 3 - 2
#done | awk '
#      {n += $1}
#END   {print n}
#' | pbcopy


for line in `cat 1.txt`; do
  fuel=$(expr $line / 3 - 2)
  while [ $fuel -gt 0 ]; do
    echo $fuel
    fuel=$(expr $fuel / 3 - 2)
  done
done | awk '
      {n += $1}
END   {print n}
' | pbcopy
