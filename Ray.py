import numpy

class Ray(object):
    def __init__(self, theta_i, p_i=(0,0), signal=1.0):
        self.theta = theta_i
        
        self.signal = signal
        self.path_length = 0
        
        self._p = p_i
        self._intersection_points = []
        
    @property
    def point(self):
        return self._p
    
    @point.setter
    def point(self, new_point):
        self._intersection_points.append(self._p)
        self._p = new_point
        
    def pol_plot(self):
        phi = numpy.asarray([i for i, j in self._intersection_points])
        rho = numpy.asarray([j for i, j in self._intersection_points])
        
        return phi, rho
        
    def car_plot(self):
        phi = numpy.asarray([i for i, j in self._intersection_points])
        rho = numpy.asarray([j for i, j in self._intersection_points])
        
        x = rho * numpy.cos(phi)
        y = rho * numpy.sin(phi)
        
        return x, y
    
if __name__ == '__main__':
    ray_ex = Ray(12, (1,2))