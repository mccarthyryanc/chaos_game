#! /usr/bin/env python
#
# Methods related to displaying Chaos Game
#

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import Image
import ngon
import ChaosGame

#screen_size = 900
#verts = 5
#dim = 2
#frac = 0.5
#max_iter = 5*10**5
screen_size = int(sys.argv[1])
verts = int(sys.argv[2])
dim = int(sys.argv[3])
frac = float(sys.argv[4])
max_iter = int(sys.argv[5])

def point2Display(point):
    return [int(float(screen_size)*(point[0]+1.0)/2.0),int(float(screen_size)*(point[1]+1.0)/2.0)]
    

def initFun():
    glClearColor(0.0,0.0,0.0,0.0)
    glColor3f(1.0,1.0,1.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0,float(screen_size),0.0,float(screen_size))

def displayFun():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POINTS)
    
    #build ngon
    new_ngon = ngon.Ngon(dim,verts)
    #play game & plot points
    points = ChaosGame.ChaosGame.play(new_ngon, frac, max_iter)
    for point in points:
        curx,cury = point2Display(point)
        #print curx,cury
        glVertex2f(curx,cury)
    
    glEnd()
    glFlush()
    screenshot = glReadPixels( 0,0, screen_size, screen_size, GL_RGBA, GL_UNSIGNED_BYTE)
    im = Image.frombuffer("RGBA", (screen_size,screen_size), screenshot, "raw", "RGBA", 0, 0)
    im.save("images/chaos_game"+"_"+str(verts)+"_"+str(frac)+".png")
    exit()

if __name__ == '__main__':
    glutInit()
    glutInitWindowSize(screen_size,screen_size)
    glutCreateWindow("Chaos Game")
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutDisplayFunc(displayFun)
    initFun()
    glutMainLoop()
    
