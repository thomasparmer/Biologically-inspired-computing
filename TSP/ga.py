#!/usr/bin/env python
import itertools
import sys
import random
import time
import math
import numpy as np
import matplotlib.pyplot as plt


start = time.time()
antByer = 24 #(min 4, max 24)
generasjoner = 20
mutchance = 0.5
crosschance = 0.5
runs = 20

argc = len(sys.argv)
if argc < 2:
    print 'usage: ', sys.argv[0], ' [file]'
    sys.exit();
        

for r in sys.argv[1:]:
    counter = 0;

    cities = [0] * antByer
    dist = [[0 for y in range(antByer)] for y in range(antByer)]

    infile = open(r, 'r')
    for line in infile:
        if counter == antByer+1:
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
#printD()

def length(l):
    lengde = 0
    for x in range(0, antByer-1):
        lengde += float(dist[l[x]][l[x+1]]) 
    return lengde


def random_start(tour_length):
    tour = range(tour_length)
    random.shuffle(tour)
    return tour


def mutate(l):
    x = random.randint(0, antByer-1)
    y = random.randint(0, antByer-1)
    z = l[x]
    l[x] = l[y]
    l[y] = z
    return l

def crossover(a):
    def tils(q):
        v = b.index(a[q])
        return v
        
    b = random_start(antByer)
    c = [-1] * antByer
    rand = random.randint(2, antByer/2)
    rand1 = random.randint(0, antByer - rand -1)
    rand2 = rand + rand1   
    i = rand1
    ant = rand2-rand1    
    while (i < rand2):
        c[i] = a[i]
        i += 1

    i = rand1
    g = tils(rand1)
    
    while (i < rand2):
        if b[i] not in c:
            if c[g] == -1:
                c[g] = b[i]
                i += 1
                g = tils(i)
            else:
                g = tils(g)
                    
        else:
            i += 1
            g = tils(i)
    for t in xrange(0, len(c)):
        if (c[t] == -1):
            c[t] = b[t]
    return c





def run(tour): 
    i = 0
    while(i < generasjoner):
        if random.random() <= crosschance:
            solution = crossover(list(tour))
            if length(solution) < length(tour):
                tour = list(solution)
        if random.random() <= mutchance:
            solution = mutate(list(tour))
            if length(solution) < length(tour):
                tour = list(solution)
        i += 1 
    return tour

def all():
    tour = random_start(antByer)
    print "start %d" % length(tour)
    worst = list(tour)
    avg = 0
    ans = [0] * runs
    best = length(tour)
    worst = length(tour)

    for y in xrange(0, runs): 
        ans[y] = run(tour)
        if length(ans[y]) < best:
            best = length(ans[y])
        if length(ans[y]) > worst:
            worst = length(ans[y])
        avg += length(ans[y])

    avg = avg/runs
    stddev = 0
    for x in xrange(0,runs):
        stddev += math.pow(length(ans[x])-avg, 2)
    stddev = math.sqrt(stddev/generasjoner)
   

    x = [0] * runs
    for y in xrange(0,runs):
        x[y] = length(ans[y])    
    plt.plot(x)
    end = time.time()
    tid = end - start
    print "Antall byer: %d\t tid brukt: %.4fs" % (antByer, tid)
    print "Beste rute: %d\t Lengste rute: %d\t Gjennomsnitt: %d\t Standardavvik: %d" % (best, worst, avg, stddev)

all()
antByer = 10
all()
antByer = 6
all()



#x = np.linspace(-2, 3, 100)

plt.title("Blue: 24 Green: 10 Red: 6")
plt.show()
