# -*- coding: utf-8 -*-

name = "satellites_name.txt"
#if len(name) < 1 : name = "satellites_name.txt"
handle = open(name)

satellites = dict()
pos = []
for line in handle:
    words = []
    #line= line.strip
    words = line.split()
    value = words.pop()
    pos = value.split('°')
    pos[0] = float(pos[0])
    if pos[1] == 'W':
        pos[0] = - pos[0]
    words.append(pos[0])
    satellites[words[0]] = words[1]

print satellites

#for k,v in satellites.items():
  #  print k,v