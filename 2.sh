#!/bin/bash

#IFS="," read -r -a array < 2.txt
#array[1]=12
#array[2]=2
#p=0
#while [[ ${array[$p]} != 99 ]]; do
#  a=${array[${array[$p+1]}]}
#  b=${array[${array[$p+2]}]}
#  if [[ ${array[$p]} == 1 ]]; then
#    array[${array[$p+3]}]=$((a+b))
#  else
#    array[${array[$p+3]}]=$((a*b))
#  fi
#  p=$((p+4))
#done
#echo ${array[0]} | pbcopy

for noun in $(seq 0 99); do
  for verb in $(seq 0 99); do
    IFS="," read -r -a array < 2.txt
    array[1]=$noun
    array[2]=$verb
    p=0
    while [[ ${array[$p]} != 99 ]]; do
      a=${array[${array[$p+1]}]}
      b=${array[${array[$p+2]}]}
      if [[ ${array[$p]} == 1 ]]; then
        array[${array[$p+3]}]=$((a+b))
      else
        array[${array[$p+3]}]=$((a*b))
      fi
      p=$((p+4))
    done
    if [[ ${array[0]} == 19690720 ]]; then
      echo $((100 * noun + verb))
      exit 0
    fi
  done
done
