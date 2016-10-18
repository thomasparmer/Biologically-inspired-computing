#!/usr/bin/env python
import itertools
import sys
import random
import time
import math

start = time.time()
argc = len(sys.argv)

antByer = 24
generasjoner = 20


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
                
def printD():
    print cities
    for z in xrange(0,antByer):
        print dist[z]

best = 0
nextAns = 0
#printD()

def length(l):
    lengde = 0
    for x in range(0, antByer-1):
        lengde += float(dist[l[x]][l[x+1]]) 
    return lengde

def hillclimb():
    def random_start(tour_length):
        tour = range(tour_length)
        random.shuffle(tour)
        return tour
    
    tour = random_start(antByer)
    mini = tour
    yes = 1
    while length(mini) < length(tour) or yes == 1:
        yes = 0
        tour = mini
        other = swapped_cities(tour)
        for i in other:
            if (length(i) < length(tour)):
                mini = i
    #print "Beste rute %d" % length(tour)
    #print tour
    return tour
    

def all_pairs(size,shuffle=random.shuffle):
    r1=range(size)
    r2=range(size)
    if shuffle:
        shuffle(r1)
        shuffle(r2)
    for i in r1:
        for j in r2:
            yield (i,j)

def swapped_cities(tour):
    '''generator to create all possible variations
      where two cities have been swapped'''
    for i,j in all_pairs(len(tour)):
        if i < j:
            copy=tour[:]
            copy[i],copy[j]=tour[j],tour[i]
            yield copy

cnt = 1
tour = hillclimb()
worst = list(tour)
avg = length(tour)
deviation = [0] * generasjoner
deviation[0] = length(tour)

while cnt < generasjoner: 
    solution = hillclimb()
    if length(solution) < length(tour):
        tour = solution
    if length(solution) > length(worst):
        worst = solution
    avg += length(solution)
    deviation[cnt] = length(solution)
    cnt += 1
avg = avg/generasjoner

stddev = 0
for x in xrange(0,20):
    stddev += math.pow(deviation[x]-avg, 2)
stddev = math.sqrt(stddev/generasjoner)

end = time.time()
tid = end-start
print "Antall byer: %d\t tid brukt: %.4fs" % (antByer, tid)
print "Beste rute: %d\t Lengste rute: %d\t Gjennomsnitt: %d\t Standardavvik: %d" % (length(tour), length(worst), avg, stddev)
