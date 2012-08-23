Chaos Game
==========

PyOpenGL implementaion of the Chaos Game. Right now you can choose: window size, dimension, the number of the vertices, fraction ("step size" for each iteration), and max number of iterations. Currently only 1D and 2D is supported (I'm working on 3D) for dimension.

Example for 1000x1000px window, 2D, with 3 vertices, a fraction of 0.5, and 5x10**5 interations:
<pre>
$ ./main.py 1000 2 3 0.5 500000
</pre>
Here is a link to an animation where the fraction varies 0.0-1.0:
https://dl.dropbox.com/u/15475461/sierpinski_animation.gif