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
 # Last modified: 2015-12-08 10:35
 #
 # Filename: plot_ite_plane.py
 #
 # Description: All Rights Are Reserved
 #
"""
import scipy as sp
import math as m
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D as Ax3
from scipy import stats as st
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

fig = plt.figure('Iter Plane Recognization')
ax = fig.gca(projection='3d')

filebuf = open('plane.csv')
data_csv = csv.reader(filebuf)

para = []
for row in data_csv:
    [para.append(float(i)) for i in row]

x = np.linspace(-150, 150, 200)
y = np.linspace(-150, 150, 200)
x, y = np.meshgrid(x, y)
z = (-x*para[0] - y*para[1] - para[3])/para[2]

mu, sigma = 0.5, 1.5
x_point = np.linspace(-100, 100, 50)
y_point = np.linspace(-100, 100, 50)
x_point, y_point = np.meshgrid(x_point, y_point)
z_point = (-x_point*para[0] - y_point*para[1] - para[3])/para[2] + np.random.normal(mu,sigma,(50,50))/8

z1 = (-x*(para[0] + 0.0009) - y*(para[1] + 0.0005) - para[3])/para[2]
z2 = (-x*(para[0] + 0.002) - y*(para[1] + 0.0005) - para[3])/para[2]
z3 = (-x*(para[0] + 0.0002) - y*(para[1] + 0.0001) - para[3])/para[2]

ax.plot_surface(x, y, z, rstride=20, cstride=20, alpha=0.8, cmap=cm.get_cmap('spring'))
ax.plot_wireframe(x, y, z1, rstride=30, cstride=30, color='cyan')
ax.plot_wireframe(x, y, z2, rstride=30, cstride=30, color='green')
ax.plot_wireframe(x, y, z3, rstride=30, cstride=30, color='r')
ax.scatter(x_point, y_point, z_point)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_zlim(-1, 1)
plt.show()
