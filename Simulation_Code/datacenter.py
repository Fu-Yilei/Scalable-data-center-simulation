# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from .End_Hosts_Structure import *
'''
Data center structure simulation for 16 host ports' switch
The introduction of Fat-Tree
'''
core_layer = []
aggregation_layer = []
edge_layer = []


end_hosts = []
for i in range(16):
    _eh = Host_structure()
    _eh.name = "EH_" + chr(i + 97)
    _eh.ip_0 = 10
    _eh.ip_1 = int(i/4)
    _eh.ip_2 = int((i%4)/2)
    _eh.ip_3 = i%4
    end_hosts.append(_eh)
    print("End Host Name: \""+ str(_eh.name)+"\", Host IP:", str(_eh.ip_0)+"."+str(_eh.ip_1)+"."+str(_eh.ip_2)+"."+str(_eh.ip_3))
edges = []

    