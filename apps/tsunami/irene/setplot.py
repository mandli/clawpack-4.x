
""" 
Set up the plot figures, axes, and items to be done for each frame.

This module is imported by the plotting routines and then the
function setplot is called to set the plot parameters.
    
"""
import os

# import numpy as np
# import matplotlib

import matplotlib.pyplot as plt
import datetime

from clawpack.visclaw import colormaps
import clawpack.clawutil.clawdata as clawdata

import clawpack.geoclaw.surge as surge

try:
    from setplotfg import setplotfg
except:
    setplotfg = None

def setplot(plotdata):
    r"""Setplot function for surge plotting"""
    

    plotdata.clearfigures()  # clear any old figures,axes,items data

    fig_num_counter = surge.plot.figure_counter()

    # Load data from output
    amrdata = clawdata.AmrclawInputData(2)
    amrdata.read(os.path.join(plotdata.outdir,'amr2ez.data'))
    # physics = clawdata.GeoclawInputData(2)
    # physics.read(os.path.join(plotdata.outdir,'geoclaw.data'))
    # surge_data = surge.data.SurgeData()
    # surge_data.read(os.path.join(plotdata.outdir,'surge.data'))
    # friction_data = surge.data.FrictionData()
    # friction_data.read(os.path.join(plotdata.outdir,'friction.data'))

    # Load storm track
    # track = surge.plot.track_data(os.path.join(plotdata.outdir,'fort.track'))

    # Calculate landfall time, off by a day, maybe leap year issue?
    # landfall_dt = datetime.datetime(2011,8,27,7,30) - datetime.datetime(2011,1,1,0)
    # landfall = (landfall_dt.days) * 24.0 * 60**2 + landfall_dt.seconds

    # Set afteraxes function
    # surge_afteraxes = lambda cd: surge.plot.surge_afteraxes(cd, 
                                        # track, landfall, plot_direction=False)
    # Limits for plots
    full_xlimits = [-85.0,-45.0]
    full_ylimits = [13.0,45.0]
    full_shrink = 0.8
    newyork_xlimits = [-74.5,-71.0]
    newyork_ylimits = [40.0,41.5]
    newyork_shrink = 0.5

    # Color limits
    surface_range = 1.5
    # speed_range = 1.0
    speed_range = 1.e-3

    xlimits = full_xlimits
    ylimits = full_ylimits
    eta = 0.0
    if not isinstance(eta,list):
        eta = [eta]
    surface_limits = [eta[0]-surface_range,eta[0]+surface_range]
    speed_limits = [0.0,speed_range]
    
    wind_limits = [0,55]
    pressure_limits = [966,1013]
    friction_bounds = [0.01,0.04]

    
    # ==========================================================================
    # ==========================================================================
    #   Plot specifications
    # ==========================================================================
    # ==========================================================================

    # ========================================================================
    #  Surface Elevations - Entire Atlantic
    # ========================================================================
    plotfigure = plotdata.new_plotfigure(name='Surface - Atlantic',  
                                         figno=fig_num_counter.get_counter())
    plotfigure.show = True

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.title = 'Surface'
    plotaxes.scaled = True
    plotaxes.xlimits = xlimits
    plotaxes.ylimits = ylimits
    
    surge.plot.add_surface_elevation(plotaxes,bounds=surface_limits,shrink=full_shrink)
    surge.plot.add_land(plotaxes)


    # ========================================================================
    #  Water Speed - Entire Atlantic
    # ========================================================================
    plotfigure = plotdata.new_plotfigure(name='Currents - Atlantic',  
                                         figno=fig_num_counter.get_counter())
    plotfigure.show = True

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.title = 'Currents'
    plotaxes.scaled = True
    plotaxes.xlimits = xlimits
    plotaxes.ylimits = ylimits

    # Speed
    surge.plot.add_speed(plotaxes,bounds=speed_limits,shrink=full_shrink)

    # Land
    surge.plot.add_land(plotaxes)


    # ========================================================================
    #  Figures for gauges
    # ========================================================================
    plotfigure = plotdata.new_plotfigure(name='Surface & topo',   
                                         figno=fig_num_counter.get_counter(),
                                         type='each_gauge')
    plotfigure.show = True
    plotfigure.clf_each_gauge = True

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    try:
        plotaxes.xlimits = [amrdata.t0,amrdata.tfinal]
    except:
        pass
    plotaxes.ylimits = surface_limits
    plotaxes.title = 'Surface'
    plotaxes.afteraxes = surge.plot.gauge_afteraxes

    # Plot surface as blue curve:
    plotitem = plotaxes.new_plotitem(plot_type='1d_plot')
    plotitem.plot_var = 3
    plotitem.plotstyle = 'r-'


    #-----------------------------------------
    
    # Parameters used only when creating html and/or latex hardcopy
    # e.g., via pyclaw.plotters.frametools.printframes:

    plotdata.printfigs = True                # print figures
    plotdata.print_format = 'png'            # file format
    plotdata.print_framenos = 'all'          # list of frames to print
    plotdata.print_gaugenos = 'all'          # list of gauges to print
    plotdata.print_fignos = 'all'            # list of figures to print
    plotdata.html = True                     # create html files of plots?
    plotdata.html_homelink = '../README.html'   # pointer for top of index
    plotdata.latex = True                    # create latex file of plots?
    plotdata.latex_figsperline = 2           # layout of plots
    plotdata.latex_framesperline = 1         # layout of plots
    plotdata.latex_makepdf = False           # also run pdflatex?

    return plotdata

