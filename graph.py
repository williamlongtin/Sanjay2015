# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 16:17:41 2022

@author: willi
"""
import pickle
from neuron import h
h.load_file("nrngui.hoc")
with open('netresults.pickle', 'rb') as f:
    net = pickle.load(f)


net.rasterplot()
net.calc_lfp()
net.pravgrates()
myg = h.Graph()
net.vlfp.plot(myg,h.dt)
myg.exec_menu("View = plot")
myg.exec_menu("New Axis")