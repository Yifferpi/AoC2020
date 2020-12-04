#! /usr/bin/env python3

f = open("input.txt", 'r')
o = open("output.txt", 'w')

pp = f.read().split("\n\n")

for s in pp:
    o.write(s.replace("\n", " ") + "\n")
