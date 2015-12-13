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
 # Last modified: 2015-12-13 18:36
 #
 # Filename: k_h_means.py
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

filebuf = open('k_means_data.txt')
filebuf2 = open('centroids.txt')
x = []
y = []
c_x1 = []
c_y1 = []
c_x2 = []
c_y2 = []
c_x3 = []
c_y3 = []
for line in filebuf.readlines():
    line = line.rstrip().split()
    x.append(float(line[0]))
    y.append(float(line[1]))
for line in filebuf2.readlines():
    line = line.rstrip().split()
    c_x1.append(float(line[0]))
    c_x2.append(float(line[2]))
    c_x3.append(float(line[4]))
    c_y1.append(float(line[1]))
    c_y2.append(float(line[3]))
    c_y3.append(float(line[5]))

fig = plt.figure('K-Harmonic Means')
ax = fig.add_subplot(111)
ax1 = fig.add_subplot(111)
ax2 = fig.add_subplot(111)
ax3 = fig.add_subplot(111)

ax.scatter(x, y, color='green', marker='s', linewidth=2)
ax1.plot(c_x1, c_y1, color='black', marker='^', linewidth=2, label='1th Centroid', ms=10)
#ax1.annotate('Convergence Direction',xy=(c_x1[0], c_y1[0]), xytext=(3.5,2.5), arrowprops=dict(facecolor='black', shrink=0.15))
ax2.plot(c_x2, c_y2, color='blue', marker='d', linewidth=2, label='2th Centroid', ms=10)
ax3.plot(c_x3, c_y3, color='brown', marker='o', linewidth=2, label='3th Centroid', ms=10)
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.legend(fontsize='medium')
plt.show()
