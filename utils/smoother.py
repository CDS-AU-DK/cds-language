#!/usr/bin/env python
import numpy as np
from scipy.optimize import curve_fit

def func(x, a, b, c, d, e):
    """Smooth help function"""
    return a*x + b*x*x + c*x*x*x +d*x*x*x*x +e

def smoother(dump):
    """A function to smooth sentiment scores over a list"""
    myInd = np.arange(len(dump))
    popt, pcov = curve_fit(func, myInd, dump)
    return [func(i,*popt) for i in myInd]

if __name__=="__main__":
    pass