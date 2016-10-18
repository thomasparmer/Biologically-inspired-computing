#!/usr/bin/env python
import itertools
import sys
import time

start = time.time()
argc = len(sys.argv)
antByer = 6

if argc < 2:
    print 'usage: ', sys.argv[0], ' [file]'
    sys.exit();
        

for r in sys.argv[1:]:
    counter = 0;

    cities = [0] * antByer
    dist = [[0 for y in range(antByer)] for y in range(antByer)]

    infile = open(r, 'r')
    for line in infile:
        if counter == antByer +1:
            break;
        else:
           
            text = line.split(';')
            for x in xrange(0,antByer):
                if counter == 0:
                    cities[x] = text[x];
                else:
                    dist[counter-1][x] = text[x];
            counter += 1;

#    print cities
#    for z in xrange(0,antByer):
#        print dist[z]

best = 0
nextAns = 0

for x in xrange(0,antByer):
    nextAns += x;


shortest = 10000000
shortestlist =[]
arr = [0] * antByer
for x in range(0, antByer):
    arr[x] = x

allperms = itertools.permutations(arr)
for l in allperms:
    solution = 0
    for x in range(0,len(l)):
        if x == len(l)-1:
            solution += float(dist[l[x]][0])
        else:
            solution += float(dist[l[x]][l[x+1]])
    #print solution
    
    if solution < shortest:
        shortest = solution
        shortestlist = l


print "Beste rute: %d" % shortest
print shortestlist
end = time.time()
tid = end - start
print "Antall byer: %d\t tid brukt: %.4fs" % (antByer, tid)
