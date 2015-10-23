import math
import numpy
        
class SemicircleTube(object):
    def __init__(self, tube_radius, turn_radius, roe, start=0, end=math.pi):
        self._diameter = 2 * float(tube_radius)   # radius
        self.roe = float(roe)  # reflectivity
        
        self._turn_radius = turn_radius    # center function
        
        self.start = start   # start of center interval
        self.end = end   # end of center interval
        
    @property
    def diameter(self):
        return self._diameter
    
    @diameter.setter
    def diameter(self, d):
        pass
    
    @property
    def turn_radius(self):
        return self._turn_radius
    
    @turn_radius.setter
    def turn_radius(self, d):
        pass
        
    def plot(self):
        """ generate plotting info. """
        phi = numpy.arange(self.start, self.end, 0.1)
        rho = numpy.asarray([self.turn_radius]*numpy.size(phi))
        
        x = rho * numpy.cos(phi)
        y = rho * numpy.sin(phi)
        return x, y
        
if __name__ == '__main__':
    c = lambda x: x**2
    tube_ex = SemicircleTube(1, 1000, 1.0, 0, math.pi*2.0)
    
    # test plot function
    import matplotlib.pyplot as mplot
    x, y =  tube_ex.plot()
    mplot.plot(x, y)
    mplot.show()