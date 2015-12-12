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
 # Last modified: 2015-12-10 16:39
 #
 # Filename: pca.py
 #
 # Description: All Rights Are Reserved
 #
"""
#import scipy as sp
#import math as m
#import matplotlib as mpl
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


fig = plt.figure('Projection of Principle Component')
ax = fig.add_subplot(111)

filebuf = open('plane.csv')
data_csv = csv.reader(filebuf)

para = []
for row in data_csv:
    [para.append(float(i)) for i in row]

mu, sigma = 0.5, 0.5
x_point = np.linspace(-100, 100, 3)
y_point = np.linspace(-100, 100, 40)
x_point, y_point = np.meshgrid(x_point, y_point)
z_point = (-x_point*para[0] - y_point*(0.01 + para[1]) - para[3])/para[2] + np.random.normal(mu,sigma, (40, 3))/8

fit_para = np.polyfit(y_point[:,0], z_point[:, 0], 1)
print fit_para
fit_x = np.linspace(-110, 110, 50)
fit_y = fit_x*fit_para[0] + fit_para[1] + 0.03
print fit_x, fit_y
ax1 = fig.add_subplot(111)
ax1.plot(fit_x, fit_y, '-', lw=1.5, color='blue')
ax.scatter(y_point, z_point, color='red', marker='*')
ax.set_xlabel('y')
ax.set_ylabel('z')
plt.show()