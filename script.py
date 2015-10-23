import math
import matplotlib.pyplot
from Ray import Ray
from Tube import SemicircleTube
import numpy

def find_point(tube, ray, a):
    phi = math.pi / 2 - ray.theta
    p_n_1 = ray.point[1]
    p_n_0 = ray.point[0] - math.pi - (2 * phi)
    return (p_n_0, p_n_1)
    
def path_length(tube, ray):
    e = 2 * ray.theta
    alpha = math.pi / 2
    phi = (alpha - ray.theta)
    
    return ((tube.turn_radius + (tube.diameter / 2.0)) * math.sin(e)) / math.sin(phi)
    
def interact(tube, ray):
    h = path_length(tube, ray)

    ray.path_length += h
    p = find_point(tube, ray, h)
    ray.point = (p[0], p[1])

def plot(tube):
    """ generate plotting info. """
    phi = numpy.arange(tube.start, tube.end, 0.1)
    rho = numpy.asarray([tube.turn_radius]*numpy.size(phi))
        
    w = (rho) * numpy.cos(phi)
    x = (rho) * numpy.sin(phi)
    
    y = (rho + 2) * numpy.cos(phi)
    z = (rho + 2) * numpy.sin(phi)
    
    return w, x, y, z
    
#define tube
tube_ex = SemicircleTube(1, 1000, 1.0, 0, math.pi*2)

#define ray
ray_ex = Ray(theta_i=.04, p_i=(math.pi,1001))

# propogate
for i in range(10):
    point = interact(tube_ex, ray_ex)

# graph
tx, ty =  tube_ex.plot()
#rx, ry =  ray_ex.pol_plot()
rrx, rry =  ray_ex.car_plot()
a,b,c,d = plot(tube_ex)

#matplotlib.pyplot.plot()
#matplotlib.pyplot.plot(rrx, rry)
#matplotlib.pyplot.plot(tx, ty)
#matplotlib.pyplot.plot(tx, ty)
#ax = matplotlib.pyplot.subplot(211, polar=True)
#ax.plot(rx, ry)

ax2 = matplotlib.pyplot.subplot(111)
ax2.plot(rrx, rry, a,b,c,d)
matplotlib.pyplot.show()