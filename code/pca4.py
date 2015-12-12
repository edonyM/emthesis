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
 # Last modified: 2015-12-10 18:42
 #
 # Filename: pca3.py
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


fig = plt.figure('Projection of Principle Component')
ax1 = fig.add_subplot(111)
ax2 = fig.add_subplot(111)
ax3 = fig.add_subplot(111)
ax4 = fig.add_subplot(111)
ax5 = fig.add_subplot(111)
ax6 = fig.add_subplot(111)
ax7 = fig.add_subplot(111)
ax8 = fig.add_subplot(111)

filebuf = open('plane.csv')
data_csv = csv.reader(filebuf)

para = []
for row in data_csv:
    [para.append(float(i)) for i in row]

mu, sigma = 0.5, 0.5
x_point = np.linspace(-100, 100, 20)
y_point = np.linspace(-100, 100, 40)
x = [i + 1.5*np.random.normal(0.3, 4.5) for i in x_point]
y = [i + 3*np.random.normal(0, 0.5) for i in y_point]

x_point, y_point = np.meshgrid(x_point, y_point)
z_point = (-x_point*para[0] - y_point*(0.01 + para[1]) - para[3])/para[2] + np.random.normal(mu,sigma, (40, 20))/8

x = [i + 1.5*np.random.normal(0.3, 4.5) for i in x_point]
y = [i + 3*np.random.normal(0, 0.5) for i in y_point]
print(len(x[0]))

ax1.scatter(x[:][:5], y[:][:5], color='cyan', marker='.')
ax2.scatter(x[:][5:10], y[5:10], color='green', marker='.')
ax3.scatter(x[:][10:15], y[:][10:15], color='yellow', marker='.')
ax4.scatter(x[:][15:20], y[:][15:20], color='blue', marker='.')
ax5.scatter(x[:][20:25], y[:][20:25], color='pink', marker='.')
ax6.scatter(x[:][25:30], y[:][25:30], color='orange', marker='.')
ax7.scatter(x[:][30:35], y[:][30:35], color='black', marker='.')
ax8.scatter(x[:][35:], y[:][35:], color='brown', marker='.')
ax1.set_xlabel('u')
ax1.set_ylabel('v')
plt.show()
