import numpy as np
from numpy import pi, cos,sin,tan,sqrt, radians,degrees

import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

from ipywidgets import *

def fun_n(sigma_t, theta):
    sigma_xp = 1/2 * (sigma_t[0,0] + sigma_t[1,1]) + \
                1/2 * (sigma_t[0,0] - sigma_t[1,1]) * cos(2 * theta) + \
                sigma_t[0,1] * sin(2 * theta)
    
    tau_xyp  = 1/2 * (- sigma_t[0,0] + sigma_t[1,1]) * sin(2 * theta) + \
                sigma_t[0,1] * cos(2 * theta)
    
    sigma_yp = 1/2 * (sigma_t[0,0] + sigma_t[1,1]) + \
                1/2 * (- sigma_t[0,0] + sigma_t[1,1]) * cos(2 * theta) - \
               sigma_t[0,1] * sin(2 * theta)
    
    sigma_tp  = np.array([[sigma_xp,tau_xyp],[tau_xyp, sigma_yp]])
    return sigma_tp
    
def fun_sigma_avg(sigma_t):
    sigma_avg = 1/2*(sigma_t[0,0] + sigma_t[1,1])
    return [sigma_avg,0]

def fun_radius(sigma_t):
    radius = sqrt((1/2*(sigma_t[0,0] - sigma_t[1,1]))**2+sigma_t[0,1]**2)
    return radius

def fun_principal_stress(sigma_avg, radius):
    return [[sigma_avg[0]+radius,0],[sigma_avg[0]-radius,0]]

def r(x,d=4):
    return round(x,d)

def axMod(fig,ax,l):
    
    fig.canvas.toolbar_visible = False
    fig.canvas.header_visible = False
    fig.canvas.resizable = False

    ax.set_aspect(1) # set aspect ratio to 1:1
    ax.set_xlim([-l,l]) # set x limit
    ax.set_ylim([-l,l]) # set x limit

    # Move left y-axis and bottim x-axis to centre, passing through (0,0)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')

    # Eliminate upper and right axes
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # Show ticks in the left and lower axes only
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # Set x and y label
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel(r'$\sigma$')

    # Position x and y label
    ax.xaxis.set_label_position("top")
    ax.yaxis.set_label_position("right")

