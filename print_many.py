#! /usr/bin/env python
#
# Script to generate many images
#

import os
import numpy as np

max_verts = 10
frac_step = 0.01

for vert in range(2,max_verts):
    for frac in np.arange(0.01,1.0,frac_step):
        if vert == 2:
            cmd = "./main.py 1000 "+str(vert)+" 1 "+str(frac)+" 500000"
        else:
            cmd = "./main.py 1000 "+str(vert)+" 2 "+str(frac)+" 500000"
        
        os.system(cmd)
    
    print "Finished Game for Verts = "+str(vert)

