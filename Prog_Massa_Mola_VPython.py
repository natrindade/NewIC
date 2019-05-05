# -*- coding: cp1252 -*-
##from time import clock
##from scipy import *
##from numpy import *
from visual import *


def massa_mola():

    # ___ VPython ___
    scene.width = 500    #336
    scene.height = 500    #375
    scene.x =860
    scene.y = 46
    scene.autoscale = 0
    scene.range = (3.,3.,3.)
    scene.center = (0,0.5,0)
    
    frame1 = frame()
    # ___ Superfície ___
    sup_x = 0.
    sup_y = 2.01
    sup_z = 0.
    sup_lenght = 7.0
    sup_heigth = 0.02
    sup_width = 7.0

    sup = box(pos=(sup_x,sup_y,sup_z),
             size=(sup_lenght,sup_heigth,sup_width),color=(0.8,0.8,0.4))

    # ___ Massa ___
    massa_x = 0.
    massa_y = 0.
    massa_z = 0.
    massa_lenght = 1.0
    massa_heigth = 1.0
    massa_width = 1.0

    massa = box(frame=frame1,pos=(massa_x,massa_y,massa_z),
                size=(massa_lenght,massa_heigth,massa_width),color=(1,1,1))

    # ___ Mola ___
    mola_x = 0.
    mola_y = 1.9
    mola_z = 0.
    mola_axis_y = - 1.3
    mola_radius = 0.3
    
    mola = helix(pos=(mola_x,mola_y,mola_z),
                 axis=(0,mola_axis_y,0),
                 coils=3,
                 radius=mola_radius) #  thickness (radius/20)

    # ___ Hastes ___
    # haste 01
    haste1_x = 0.
    haste1_y = 2.
    haste1_z = 0.
    haste1_axis_y = -0.1
    haste1_radius = 0.5*(mola_radius/20.) # helix default thickness (radius/20)
    
    haste1 = cylinder(pos=(haste1_x,haste1_y,haste1_z),
                      axis=(0.,haste1_axis_y,0.),radius = haste1_radius,
                      color=(1,1,1))
    # haste 02
    haste2_y = massa_y + mola_y + mola_axis_y # 0.6
    
    haste2 = cylinder(frame=frame1,pos=(haste1_x,haste2_y,haste1_z),
                      axis=(0.,haste1_axis_y,0.),radius = haste1_radius,
                      color=(1,1,1))
    # haste 03
    haste3_y = haste1_y + haste1_axis_y
    haste3_axis_z = - mola_radius
    
    haste3 = cylinder(pos=(haste1_x,haste3_y,haste1_z),
                      axis=(0.,0.,haste3_axis_z),radius = haste1_radius,
                      color=(1,1,1))
    # haste 04
    haste4 = cylinder(frame=frame1,pos=(haste1_x,haste2_y,haste1_z),
                      axis=(0.,0.,haste3_axis_z),radius = haste1_radius,
                      color=(1,1,1))

    return mola, haste1, haste2, haste3, haste4, massa, frame1

##mola, haste1, haste2, haste3, haste4, massa, frame1 = massa_mola()
