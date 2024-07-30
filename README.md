This is a simple graphics library made to work inside most terminals that support ansi escape codes.  
It currently supports vertecies, lines and triangles from which more complex shapes can be built up.  
It requires further optimizations since drawing big shapes causes significant lag.

How to use:
  To create a point on screen
    -create new Vertex object passing xyz coordinates as constructor parameters.
    -call vertex.updateSelf()
    -add the vertex into scene array
    -call drawpoints function which will display all objects from the scene array. 
    
  To create a line
    -create 2 new Vertecies as shown above and than create a Line object without any constructor parameters
    -call line.setEnds() and pass 2 vertex objects as parameters (the 2 ends of the line)
    -call line.visCheck()
    -call line.calcSlope()
    -add the line to scene array and call drawpoints()
    
  To create a triangle
    -create 3 points as shown above,
    -create 3 lines as shown above,
    -createa  Tri object without constructor parameters,
    -call tir.setEdges() passing the 3 created lines as parameters. The 3 lines must form an closed triangle else exception is raised.
    -add the triangle  to scene  and call drawpoints()  


Function explanations
**vertex.updateSelf()** takes 0 parameters, converts real xyz coordines of  the point to screen space (row and column). IF the point is outside the screen (x or y is outside viewable area)
                                            **prevents** the point from being drawn **until** the next call to updateSelf() during which point is visible 
                                            
**vertex.set X/Y/Z(v)** takes 1 parameter,  sets the X/Y/Z coordiante of the vertex to V in real space, requires call to **vertex.updateSelf()**  for changes to take effect
**vertex.get X/Y/Z()**       takes 0 parameters, returns X/Y/Z coordinate of the vertex in real space



**line.setEnds(v1, v2)** takes 2 parameters, sets ends of line to v1 and v2 where v1 & v2 are Vertex objects
**line.calcSlope()**     takes 0 parameters, calculates the slope  of the line  which is required for displaying
**line.visCheck()**           takes 0 parameters, Calls visCheck() of both ends of the line. in case both of the points are outside screen prevents the line from drawn untill next visCheck() call  when at least one point is visible



**tri.setEdges(l1, l2, l3)** takes 3 parameters, sets edges of a triangle to l1, l2 and l3.  In case the 3 lines do not share 3 mutual vertecies it will raise an exception.
                                                  Its recommended to create only 3 vertecies and use them among the edges instead of creating 2 vertecies for each line. 


**vertex/line/tri.setColor(r,g,b)** takes 3 parameters, sets color of the object to rgb values passed in as parameters. Might have issues on terminal emulators that do not support full 24bit color range;



**scene[]** Scene array stores all objects currently insdie the "scene". Any object (vertex, line, triangle) inside it will be drawn to screen when the drawPoints() is called.
**drawPoints()**  Draws all objects from the scene array to the screen.



    
