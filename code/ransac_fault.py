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
 # Last modified: 2015-12-03 15:32
 #
 # Filename: breakdown.py
 #
 # Description: All Rights Are Reserved
 #
"""
#import scipy as sp
#import math as m
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D as Ax3
#from scipy import stats as st
from matplotlib import cm
import numpy as np
import csv

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
x1 = np.linspace(3000, 5000, 21)
x2 = np.linspace(5100, 10000, 49)
x3 = np.linspace(10000, 14000, 49)
x4 = np.linspace(14000, 16000, 21)
x5 = np.linspace(16000, 18000, 21)
y1 = 1000000.0/(((x1-2500)/1.2)**3) + 0.04 #cone
y1_2 = np.exp((x2)/(1000*np.exp(np.pi)))/30.0 - 0.0024
y1_3 = (x3-10500)**2/10000000000.0 + 0.0484
y1_4 = (0.0496-(x4-14000)**2)/1000000000.0 + 0.0496
y1_5 = (x5-16000)/10000000.0 + 0.044

tmp1 = list(x1)
tmp2 = list(x2)
tmp3 = list(x3)
tmp4 = list(x4)
tmp5 = list(x5)
tmp1.extend(tmp2)
tmp1.extend(tmp3)
tmp1.extend(tmp4)
tmp1.extend(tmp5)
pos = [tmp1.index(x2[0]), tmp1.index(x5[1])]
x_t = np.array(tmp1)
tmp1 = list(y1)
tmp2 = list(y1_2)
tmp3 = list(y1_3)
tmp4 = list(y1_4)
tmp5 = list(y1_5)
tmp1.extend(tmp2)
tmp1.extend(tmp3)
tmp1.extend(tmp4)
tmp1.extend(tmp5)
y_t = np.array(tmp1)

y_t = [i+np.random.normal(-0.02, 0.04)/155.0 for i in y_t]
y_t = [1000000*(2*0.052-i) for i in y_t]

x_p = [x2[0],x5[1]]
y_p = [y_t[pos[0]], y_t[pos[1]]]
ax.plot(x_t, y_t, color='cyan', marker='.', markersize=2)
ax1.scatter(np.array(x_p)[0], np.array(y_p)[0], marker='v', color='r', s=40, label='Local Optimze')
ax2.scatter(np.array(x_p)[1], np.array(y_p)[1], marker='s', color='g', s=40, label='Global Optimze')
plt.legend()
ax.set_xlabel('Number of Iteration')
ax.set_ylabel('Number of Feature Point Cloud')
plt.show()
