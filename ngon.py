#! /usr/bin/env python
#
# Methods related to n-gons
#
import sys, re, random
import numpy as np

#Method to generate vertices of N-Gon
def generate_ngon(dim, vert_num):
    
    verts = []
    
    if dim == 1:
        verts = [[-1.0,0.0],[1.0,0.0]]
    elif dim == 2:
        angle_step = 2.0*np.pi/float(vert_num)
        angle = 0.0
        for i in range(int(vert_num)):
            x = np.cos(angle)
            y = np.sin(angle)
            verts.append([x,y])
            angle += angle_step
        
    elif dim == 3:
        print "Not yet"
    
    return verts


def point_in_poly(x,y,poly):
    poly.reverse()
    n = len(poly)
    inside = False

    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x,p2y = poly[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x,p1y = p2x,p2y

    return inside

class Ngon:
    def __init__(self,dim,vert_num):
        if dim == 1 and vert_num != 2:
            print "When in 1-D, there can only be 2 vertices!"
            exit()
        
        self.dim = dim
        self.vert_num = vert_num
        self.verts = generate_ngon(dim, vert_num)
    
    def rand_vert(self):
        return random.choice(self.verts)
        
    def rand_in(self):
        if self.dim == 1:
            return [random.uniform(-1.0,1.0),0.0]
        else:
            inside = False
            while not inside:
                x = random.uniform(-1.0,1.0)
                random.seed()
                y = random.uniform(-1.0,1.0)
                inside = point_in_poly(x,y,self.verts)
            
            return [x,y]
