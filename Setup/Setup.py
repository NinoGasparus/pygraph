import  os


nx = -5
px =  5
ny = -2
py =  2
plane = {"nx": nx, "px": px, "ny" : ny, "py" : py}
screensize ={"x" : 0 , "y" : 0 }  
yshrink = 0.75
def init():
    screensize["x"]= os.get_terminal_size().columns-1
    screensize["y"]= os.get_terminal_size().lines

    #Characters in terminal are usually taller than wide. So overall image is shrunk over the Y axis
    yshrink = 0.75
    


def setSize(a, b, c, d):
    nx = a
    px = b
    ny = c
    py = d
    plane = {"nx": nx, "px": px, "ny" : ny, "py" : py}
