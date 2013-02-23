
"""
Module to create topo and qinit data files for this example.
"""

from clawpack.geoclaw import topotools
from numpy import *

def maketopo():
    """
    Output topography file for the entire domain
    """
    nxpoints = 201
    nypoints = 201
    xlower = -100.e3
    xupper = 100.e3
    yupper = 100.e3
    ylower = -100.e3
    outfile= "bowl.topotype2"     
    topotools.topo2writer(outfile,topo,xlower,xupper,ylower,yupper,nxpoints,nypoints)

def makeqinit():
    """
    Create qinit data file
    """
    nxpoints = 101
    nypoints = 101
    xlower = -50.e0
    xupper = 50.e0
    yupper = 50.e0
    ylower = -50.e0
    outfile= "hump.xyz"     
    topotools.topo1writer(outfile,qinit,xlower,xupper,ylower,yupper,nxpoints,nypoints)

def topo(x,y):
    """
    Parabolic bowl
    """
    # value of z at origin:  Try zmin = 80 for shoreline or 250 for no shore
    zmin = 2e3
    z = 2.5e-7*(x**2 + y**2) - zmin
    return z


def qinit(x,y):
    """
    Gaussian hump:
    """
    z = 0.1 * exp(-(x + y)**2 / 1e6)
    return z

if __name__=='__main__':
    maketopo()
    makeqinit()
