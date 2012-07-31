#! /usr/bin/env python
#
# Methods to generate the points while playing The Chaos Game
#
import sys, re, random
import numpy as np

max_iter = 10**8

class ChaosGame:
    
    #method to play 
    @staticmethod
    def play(ngon,frac):
        points = []
        i = 0
        x1,y1 = ngon.rand_in()
        while i <= max_iter:
            x2,y2 = ngon.rand_vert()
            x1 = x1 + (x2-x1)*frac
            y1 = y1 + (y2-y1)*frac
            if i > 100:
                points.append([x1,y1])
                
            i++
            
        return points
        
