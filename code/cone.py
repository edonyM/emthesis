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
 # Last modified: 2015-12-02 13:01
 #
 # Filename: cone.py
 #
 # Description: All Rights Are Reserved
 #
"""
#import scipy as sp
#import math as m
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#from scipy import stats as st
from matplotlib import cm
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

from mpl_toolkits.mplot3d import Axes3D
def euler_rot(XYZ,phi,theta,psi):
    '''Returns the points XYZ rotated by the given euler angles'''


    ERot = np.array([[np.cos(theta)*np.cos(psi), 
                      -np.cos(phi)*np.sin(psi) + np.sin(phi)*np.sin(theta)*np.cos(psi), 
                      np.sin(phi)*np.sin(psi) + np.cos(phi)*np.sin(theta)*np.cos(psi)],
                     [np.cos(theta)*np.sin(psi), 
                      np.cos(phi)*np.cos(psi) + np.sin(phi)*np.sin(theta)*np.sin(psi),
                      -np.sin(phi)*np.cos(psi) + np.cos(phi)*np.sin(theta)*np.sin(psi)],
                     [-np.sin(theta),
                      np.sin(phi)*np.cos(theta),
                      np.cos(phi)*np.cos(theta)]])

    return ERot.dot(XYZ)


u = np.linspace(0,2*np.pi,50)
num_levels = 10

r0 = 1 # maximum radius of cone
h0 = 5 # height of cone

phi = .5 # aka alpha
theta = .25 # aka beta
psi = 0 # aka gamma



norm = np.array([0,0,h0]).reshape(3,1)
normp = euler_rot(norm,phi,theta,psi)


fig = plt.figure("cone")
ax = fig.add_subplot(111, projection='3d')

ax.plot([0,normp[0]],[0,normp[1]],zs= [0,normp[2]])

x = np.hstack([r0*(1-h)*np.cos(u) for h in np.linspace(0,1,num_levels)])
y = np.hstack([r0*(1-h)*np.sin(u) for h in np.linspace(0,1,num_levels)])
z = np.hstack([np.ones(len(u))*h*h0 for h in np.linspace(0,1,num_levels)])
XYZ = np.vstack([x,y,z])

xp,yp,zp = euler_rot(XYZ,phi,theta,psi) 
ax.plot_wireframe(xp,yp,zp)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
