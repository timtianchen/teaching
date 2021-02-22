import numpy as np
from numpy import pi, cos,sin,tan,sqrt, radians,degrees

import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

from ipywidgets import *

def fun_n(sigma_t, theta):
    sigma_xxp = 1/2 * (sigma_t[0,0] + sigma_t[1,1]) + \
                1/2 * (sigma_t[0,0] - sigma_t[1,1]) * cos(2 * theta) + \
                sigma_t[0,1] * sin(2 * theta)
    
    tau_xyp   = 1/2 * (- sigma_t[0,0] + sigma_t[1,1]) * sin(2 * theta) + \
                sigma_t[0,1] * cos(2 * theta)
    
    sigma_yyp = 1/2 * (sigma_t[0,0] + sigma_t[1,1]) + \
                1/2 * (- sigma_t[0,0] + sigma_t[1,1]) * cos(2 * theta) - \
               sigma_t[0,1] * sin(2 * theta)
    
    return [sigma_xxp,tau_xyp,sigma_yyp]
    
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

