import numpy
def intensity(theta,y):#    return param_vals[0] + param_vals[1]*x**2
    ans =(numpy.sin(numpy.pi*(a/y) * numpy.sin(theta)))/ (numpy.pi * (a/y) * numpy.sin(theta))**2 * (numpy.cos(numpy.pi * (d/y)*numpy.sin(theta)))**2
    z = 10*numpy.log10(ans)
    return z

