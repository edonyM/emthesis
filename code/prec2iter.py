#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
 #        .---.         .-----------
 #       /     \  __  /    ------
 #      / /     \(  )/    -----   (`-')  _ _(`-')              <-. (`-')_
 #     //////    '\/ `   ---      ( OO).-/( (OO ).->     .->      \( OO) )     .->
 #    //// / //  :   : ---      (,------. \    .'_ (`-')----. ,--./ ,--/  ,--.'  ,-.
 #   // /   /  / `\/ '--         |  .---' '`'-..__)( OO).-. ' |   \ |  | (`-')'.'  /
 #  //          //..\\          (|  '--.  |  |  ' |( _) | | | |  . '|  |)(OO \    /
 # ============UU====UU====      |  .--'  |  |  / : \|  |)| | |  |\    |  |  /   /)
 #             '//||\\`          |  `---. |  '-'  /  '  '-' ' |  | \   |  `-/   /`
 #               ''``            `------' `------'    `-----' `--'  `--'    `--'
 # ######################################################################################
 #
 # Author: edony - edonyzpc@gmail.com
 #
 # twitter : @edonyzpc
 #
 # Last modified: 2015-12-08 21:09
 #
 # Filename: prec2iter.py
 #
 # Description: All Rights Are Reserved
 #
"""
#import scipy as sp
#import math as m
#import matplotlib as mpl
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D as Ax3
#from scipy import stats as st
#from matplotlib import cm
import numpy as np

class PyColor(object):
    """ This class is for colored print in the python interpreter!
    "F3" call Addpy() function to add this class which is defined
    in the .vimrc for vim Editor."""
    def __init__(self):
        self.self_doc = r"""
        STYLE: \033['display model';'foreground';'background'm
        DETAILS:
        FOREGROUND        BACKGOUND       COLOR
        ---------------------------------------
        30                40              black
        31                41              red
        32                42              green
        33                43              yellow
        34                44              blue
        35                45              purple
        36                46              cyan
        37                47              white
        DISPLAY MODEL    DETAILS
        -------------------------
        0                default
        1                highlight
        4                underline
        5                flicker
        7                reverse
        8                non-visiable
        e.g:
        \033[1;31;40m   <!--1-highlight;31-foreground red;40-background black-->
        \033[0m         <!--set all into default-->
        """
        self.warningcolor = '\033[0;31m'
        self.tipcolor = '\033[0;32m'
        self.endcolor = '\033[0m'
        self._newcolor = ''
    @property
    def new(self):
        """
        Customized Python Print Color.
        """
        return self._newcolor
    @new.setter
    def new(self, color_str):
        """
        New Color.
        """
        self._newcolor = color_str
    def disable(self):
        """
        Disable Color Print.
        """
        self.warningcolor = ''
        self.endcolor = ''

fig = plt.figure('Precision VS Iterations')
ax = fig.add_subplot(111)
ax1 = fig.add_subplot(111)
ax2 = fig.add_subplot(111)
x = np.arange(3000, 10000, 100)
x1 = np.linspace(3000, 5000, 21)
x2 = np.linspace(5100, 10000, 49)
y1 = 1000000.0/(((x1-2500)/1.2)**3) + 0.04 #cone
y1_2 = np.exp((x2)/(1000*np.exp(np.pi)))/30.0 - 0.0024
y2 = 200000.0/(x**2) + 0.03 #suntou
y3 = 100000.0/(3*(x**2)) + 0.03#plane
y1 = [i+np.random.normal(-0.02, 0.04)/150.0 for i in y1]
y1_2 = [i+np.random.normal(-0.02, 0.04)/135.0 for i in y1_2]
y2 = [i+np.random.normal(-0.02, 0.04)/100.0 for i in y2]
y3 = [i+np.random.normal(-0.02, 0.04)/95.0 for i in y3]

tmp1 = list(x1)
tmp2 = list(x2)
tmp1.extend(tmp2)
x_t = np.array(tmp1)
tmp1 = list(y1)
tmp2 = list(y1_2)
tmp1.extend(tmp2)
y_t = np.array(tmp1)
ax.plot(x_t, y_t, color='green', label='Large-scale Parts')
ax1.plot(x, y2, color='blue', label='Normal Tenon')
ax2.plot(x, y3, color='red', label='Plane')
ax.set_xlabel("Iterations")
ax.set_ylabel("Model Precision")
plt.legend()
plt.grid(True)
plt.show()
