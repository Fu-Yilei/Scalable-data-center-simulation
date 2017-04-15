# -*- coding: utf-8 -*-



#Data center structure simulation for 16 host ports' switch

#The introduction of Fat-Tree
#Structure of End Host

K = 4 #PODS NUMBER

print("\nWe have", K, "Pods")
class IP_Address: #IP Structure
    def __init__(self):
        self.ip_0 = 10   
        self.ip_1 = 2
        self.ip_2 = 1   
        self.ip_3 = 1  
        
class End_Host_structure: #End_Host
    def __init__(self):
        self.name = ''
        self.ip = IP_Address()
        
class Core_Switch_Structure: #Core_Switch
    def __init__(self):
        self.name = ''
        self.ip = IP_Address()
       
class Pod_Switch_Structure:
    def __init__(self):
        self.name = ''
        self.ip = IP_Address()
        


end_hosts = []
for i in range(int(4*(K/2)**2)):
    _eh = End_Host_structure()
    _eh.name = "EH_" + chr(i + 97)
    _eh.ip.ip_0 = 10
    _eh.ip.ip_1 = int(i/4) #current pod
    _eh.ip.ip_2 = int((i%4)/2) #current switch
    _eh.ip.ip_3 = int(2+i%(K/2))
    end_hosts.append(_eh)
    print("End Host Name: \""+ str(_eh.name)+"\", Host IP:", str(_eh.ip.ip_0)+"."+str(_eh.ip.ip_1)+"."+str(_eh.ip.ip_2)+"."+str(_eh.ip.ip_3))
print()

switchs = []
for i in range(K*4):
    _ps = Pod_Switch_Structure()
    _ps.name = "PS_" + chr(i + 97)
    _ps.ip.ip_0 = 10
    _ps.ip.ip_1 = int(i/4)
    _ps.ip.ip_2 = i%4
    _ps.ip.ip_3 = 1
    switchs.append(_ps)
    print("Pod Switch Name: \""+ str(_ps.name)+"\", Host IP:", str(_ps.ip.ip_0)+"."+str(_ps.ip.ip_1)+"."+str(_ps.ip.ip_2)+"."+str(_ps.ip.ip_3))

print()
core_switchs = []
for i in range(int((K/2)**2)):
    _cs = Core_Switch_Structure()
    _cs.name =  "CS_" + chr(i + 97)
    _cs.ip.ip_0 = 10
    _cs.ip.ip_1 = K
    _cs.ip.ip_2 = 1+int(i/(K/2))
    _cs.ip.ip_3 = 1+int(i%(K/2))
    core_switchs.append(_cs)
    print("Core Switch Name: \""+ str(_cs.name)+"\", Switch IP:", str(_cs.ip.ip_0)+"."+str(_cs.ip.ip_1)+"."+str(_cs.ip.ip_2)+"."+str(_cs.ip.ip_3))
