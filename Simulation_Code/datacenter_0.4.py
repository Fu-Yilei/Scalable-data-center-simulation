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
        
class Prefix_structure:
    def __init__(self):
        self.SwitchAdress = IP_Address()
        self.prefix = IP_Address()
        self.port = 0

class Suffix_structure:
    def __init__(self):
        self.SwitchAdress = IP_Address()
        self.suffix = IP_Address()
        self.port = 0
        
class Routing_table:
    def __init__(self):
        self.PrefixTable = Prefix_structure()
        self.SuffixTable = Suffix_structure()

class End_Host_structure: #End_Host
    def __init__(self):
        self.name = ''
        self.ip = IP_Address()
        self.state = 0
        
class Core_Switch_Structure: #Core_Switch
    def __init__(self):
        self.name = ''
        self.ip = IP_Address()
        self.state = 0
       
class Pod_Switch_Structure:
    def __init__(self):
        self.name = ''
        self.ip = IP_Address()
        self.state = 0

'''        
class Port_To_Address_table:
    def __init__(self):
        self.SwitchAdress = IP_Address()
        self.port = 0
        self.ForwardAddress = IP_Address()
'''

end_hosts = []
for i in range(int(4*(K/2)**2)):
    _eh = End_Host_structure()
    _eh.name = "EH_" + chr(i + 97)
    _eh.ip.ip_0 = 10
    _eh.ip.ip_1 = int(i/4) #current pod
    _eh.ip.ip_2 = int((i%4)/2) #current switch
    _eh.ip.ip_3 = int(2+i%(K/2))
    end_hosts.append(_eh)
    print("End Host Name: \""
          + str(_eh.name)+
          "\", Host IP:",
          str(_eh.ip.ip_0)+
          "."+str(_eh.ip.ip_1)+
          "."+str(_eh.ip.ip_2)+
          "."+str(_eh.ip.ip_3))
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
    print("Pod Switch Name: \""+ 
          str(_ps.name)+
          "\", Host IP:",
          str(_ps.ip.ip_0)+
          "."+str(_ps.ip.ip_1)+
          "."+str(_ps.ip.ip_2)+
          "."+str(_ps.ip.ip_3))
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
    print("Core Switch Name: \""+
          str(_cs.name)+
          "\", Switch IP:",
          str(_cs.ip.ip_0)+
          "."+str(_cs.ip.ip_1)+
          "."+str(_cs.ip.ip_2)+
          "."+str(_cs.ip.ip_3))
print()

#=================================================  
#Routing Algorithm

#Lower Pod Switch Table
lower_pod_tables = []
print("Lower Pod Switches Routing Table:")
print("Pod Switch Address | Prefix/Suffix | Port")
for x in range(0,K):
    for z in range(int(K/2)):
        _lpt = Routing_table()
        _lpt.PrefixTable.SwitchAdress.ip_0 = 10
        _lpt.PrefixTable.SwitchAdress.ip_1 = x
        _lpt.PrefixTable.SwitchAdress.ip_2 = z
        _lpt.PrefixTable.SwitchAdress.ip_3 = 1
        _lpt.PrefixTable.prefix.ip_0 = 0
        _lpt.PrefixTable.prefix.ip_1 = 0
        _lpt.PrefixTable.prefix.ip_2 = 0
        _lpt.PrefixTable.prefix.ip_3 = 0
        _lpt.PrefixTable.port = 0
        lower_pod_tables.append(_lpt)
        print("      "+str(_lpt.PrefixTable.SwitchAdress.ip_0)+
              "."+str(_lpt.PrefixTable.SwitchAdress.ip_1)+
              "."+str(_lpt.PrefixTable.SwitchAdress.ip_2)+
              "."+str(_lpt.PrefixTable.SwitchAdress.ip_3)+
              " |  "+str(_lpt.PrefixTable.prefix.ip_0)+
              "."+str(_lpt.PrefixTable.prefix.ip_1)+
              "."+str(_lpt.PrefixTable.prefix.ip_2)+
              "."+str(_lpt.PrefixTable.prefix.ip_3)+
              " | "+str(_lpt.PrefixTable.port))
        
        for i in range(2,int(K/2+2)):
            _lpt.SuffixTable.SwitchAdress.ip_0 = 10
            _lpt.SuffixTable.SwitchAdress.ip_1 = x
            _lpt.SuffixTable.SwitchAdress.ip_2 = z
            _lpt.SuffixTable.SwitchAdress.ip_3 = 1
            _lpt.SuffixTable.suffix.ip_0 = 0
            _lpt.SuffixTable.suffix.ip_1 = 0
            _lpt.SuffixTable.suffix.ip_2 = 0
            _lpt.SuffixTable.suffix.ip_3 = i
            _lpt.SuffixTable.port = int((i-2+z)%(K/2)+(K/2))
            lower_pod_tables.append(_lpt)
            print("      "+str(_lpt.SuffixTable.SwitchAdress.ip_0)+
                  "."+str(_lpt.SuffixTable.SwitchAdress.ip_1)+
                  "."+str(_lpt.SuffixTable.SwitchAdress.ip_2)+
                  "."+str(_lpt.SuffixTable.SwitchAdress.ip_3)+
                  " |  "+str(_lpt.SuffixTable.suffix.ip_0)+
                  "."+str(_lpt.SuffixTable.suffix.ip_1)+
                  "."+str(_lpt.SuffixTable.suffix.ip_2)+
                  "."+str(_lpt.SuffixTable.suffix.ip_3)+
                  " | "+str(_lpt.SuffixTable.port))
print()

#Upper Pod Switch Table
upper_pod_tables = []
print("Upper Pod Switches Routing Table:")
print("Pod Switch Address | Prefix/Suffix | Port")
for x in range(0,K):
    for z in range(int(K/2),K):
        for i in range(0,int(K/2)):
            _upt = Routing_table()
            _upt.PrefixTable.SwitchAdress.ip_0 = 10
            _upt.PrefixTable.SwitchAdress.ip_1 = x
            _upt.PrefixTable.SwitchAdress.ip_2 = z
            _upt.PrefixTable.SwitchAdress.ip_3 = 1
            _upt.PrefixTable.prefix.ip_0 = 10
            _upt.PrefixTable.prefix.ip_1 = x
            _upt.PrefixTable.prefix.ip_2 = i
            _upt.PrefixTable.prefix.ip_3 = 0
            _upt.PrefixTable.port = i
            upper_pod_tables.append(_upt)
            print("      "+str(_upt.PrefixTable.SwitchAdress.ip_0)+
                  "."+str(_upt.PrefixTable.SwitchAdress.ip_1)+
                  "."+str(_upt.PrefixTable.SwitchAdress.ip_2)+
                  "."+str(_upt.PrefixTable.SwitchAdress.ip_3)+
                  " | "+str(_upt.PrefixTable.prefix.ip_0)+
                  "."+str(_upt.PrefixTable.prefix.ip_1)+
                  "."+str(_upt.PrefixTable.prefix.ip_2)+
                  "."+str(_upt.PrefixTable.prefix.ip_3)+
                  " | "+str(_upt.PrefixTable.port))
        
        _upt.PrefixTable.SwitchAdress.ip_0 = 10
        _upt.PrefixTable.SwitchAdress.ip_1 = x
        _upt.PrefixTable.SwitchAdress.ip_2 = z
        _upt.PrefixTable.SwitchAdress.ip_3 = 1
        _upt.PrefixTable.prefix.ip_0 = 0
        _upt.PrefixTable.prefix.ip_1 = 0
        _upt.PrefixTable.prefix.ip_2 = 0
        _upt.PrefixTable.prefix.ip_3 = 0
        _upt.PrefixTable.port = 0
        upper_pod_tables.append(_upt)
        print("      "+str(_upt.PrefixTable.SwitchAdress.ip_0)+
              "."+str(_upt.PrefixTable.SwitchAdress.ip_1)+
              "."+str(_upt.PrefixTable.SwitchAdress.ip_2)+
              "."+str(_upt.PrefixTable.SwitchAdress.ip_3)+
              " |  "+
              str(_upt.PrefixTable.prefix.ip_0)+
              "."+str(_upt.PrefixTable.prefix.ip_1)+
              "."+str(_upt.PrefixTable.prefix.ip_2)+
              "."+str(_upt.PrefixTable.prefix.ip_3)+
              " | "+str(_upt.PrefixTable.port))
        
        for i in range(2,int(K/2+2)):
            _upt = Routing_table()
            _upt.SuffixTable.SwitchAdress.ip_0 = 10
            _upt.SuffixTable.SwitchAdress.ip_1 = x
            _upt.SuffixTable.SwitchAdress.ip_2 = z
            _upt.SuffixTable.SwitchAdress.ip_3 = 1
            _upt.SuffixTable.suffix.ip_0 = 0
            _upt.SuffixTable.suffix.ip_1 = 0
            _upt.SuffixTable.suffix.ip_2 = 0
            _upt.SuffixTable.suffix.ip_3 = i
            _upt.SuffixTable.port = int((i-2+z)%(K/2)+(K/2))
            upper_pod_tables.append(_upt)
            print("      "+str(_upt.SuffixTable.SwitchAdress.ip_0)+
                  "."+str(_upt.SuffixTable.SwitchAdress.ip_1)+
                  "."+str(_upt.SuffixTable.SwitchAdress.ip_2)+
                  "."+str(_upt.SuffixTable.SwitchAdress.ip_3)+
                  " |  "+str(_upt.SuffixTable.suffix.ip_0)+
                  "."+str(_upt.SuffixTable.suffix.ip_1)+
                  "."+str(_upt.SuffixTable.suffix.ip_2)+
                  "."+str(_upt.SuffixTable.suffix.ip_3)+
                  " | "+str(_upt.SuffixTable.port))
print()

#Core Swich Table
core_tables = []
_ct = Prefix_structure()
print("Core Switches Routing Table:")
print("Core Switch Address | Prefix | Port")
for j in range(1,int(K/2+1)):
    for i in range(1,int(K/2+1)):
        for x in range(K):
            _ct = Prefix_structure()
            _ct.SwitchAdress.ip_0 = 10
            _ct.SwitchAdress.ip_1 = K
            _ct.SwitchAdress.ip_2 = j
            _ct.SwitchAdress.ip_3 = i
            _ct.prefix.ip_0 = 10
            _ct.prefix.ip_1 = x
            _ct.prefix.ip_2 = 0
            _ct.prefix.ip_3 = 0
            _ct.port = x
            core_tables.append(_ct)
            print("      "+str(_ct.SwitchAdress.ip_0)+
                  "."+str(_ct.SwitchAdress.ip_1)+
                  "."+str(_ct.SwitchAdress.ip_2)+
                  "."+str(_ct.SwitchAdress.ip_3)+
                  " | "+str(_ct.prefix.ip_0)+
                  "."+str(_ct.prefix.ip_1)+
                  "."+str(_ct.prefix.ip_2)+
                  "."+str(_ct.prefix.ip_3)+
                  " | "+str(_ct.port))
print()

#==========================================
#Routing Simulation

Source_Host_IP = IP_Address()
Source_Host_IP.ip_0 = 10
Source_Host_IP.ip_1 = 0
Source_Host_IP.ip_2 = 1
Source_Host_IP.ip_3 = 2
Destination_Host_IP = IP_Address()
Destination_Host_IP.ip_0 = 10
Destination_Host_IP.ip_0 = 2
Destination_Host_IP.ip_0 = 0
Destination_Host_IP.ip_0 = 3

def Routing_Algorithm():
    #Step 1
    for i in range(K*4):
        if switchs[i].ip.ip_1 == Source_Host_IP.ip_1 \
        and switchs[i].ip.ip_2 == Source_Host_IP.ip_2:
            switchs[i].state = 1
            print(str(switchs[i].ip.ip_0)+
                  "."+str(switchs[i].ip.ip_1)+
                  "."+str(switchs[i].ip.ip_2)+
                  "."+str(switchs[i].ip.ip_3))
    
    #Step 2 
    #print(lower_pod_tables[2].SuffixTable.SwitchAdress.ip_2)
    for n in range(K*4):
        if switchs[n].state == 1:
            '''
            print(str(switchs[n].ip.ip_0)+
                  "."+str(switchs[n].ip.ip_1)+
                  "."+str(switchs[n].ip.ip_2)+
                  "."+str(switchs[n].ip.ip_3))  
            '''
            for i in range(len(lower_pod_tables)):
                '''
                print("      "+str(lower_pod_tables[i].SuffixTable.SwitchAdress.ip_0)+
                      "."+str(lower_pod_tables[i].SuffixTable.SwitchAdress.ip_1)+
                      "."+str(lower_pod_tables[i].SuffixTable.SwitchAdress.ip_2)+
                      "."+str(lower_pod_tables[i].SuffixTable.SwitchAdress.ip_3)+
                      " |  "+str(lower_pod_tables[i].SuffixTable.suffix.ip_0)+
                      "."+str(lower_pod_tables[i].SuffixTable.suffix.ip_1)+
                      "."+str(lower_pod_tables[i].SuffixTable.suffix.ip_2)+
                      "."+str(lower_pod_tables[i].SuffixTable.suffix.ip_3)+
                      " | "+str(lower_pod_tables[i].SuffixTable.port))
                print(lower_pod_tables[i].SuffixTable.SwitchAdress.ip_1)
                '''
                if switchs[n].ip.ip_1 == lower_pod_tables[i].SuffixTable.SwitchAdress.ip_1 \
                and switchs[n].ip.ip_2 == lower_pod_tables[i].SuffixTable.SwitchAdress.ip_2:
                    for m in range(K*4):
                        if switchs[m].ip.ip_2 == lower_pod_tables[i].SuffixTable.port \
                        and switchs[m].ip.ip_1 == lower_pod_tables[i].SuffixTable.SwitchAdress.ip_1:
                            switchs[m].state = 2
                            print(str(switchs[m].ip.ip_0)+
                                  "."+str(switchs[m].ip.ip_1)+
                                  "."+str(switchs[m].ip.ip_2)+
                                  "."+str(switchs[m].ip.ip_3))
                            return   
    #Step3
    for n in range(K*4):
        if switchs[n].state == 2:
            
            print(str(switchs[n].ip.ip_0)+
                  "."+str(switchs[n].ip.ip_1)+
                  "."+str(switchs[n].ip.ip_2)+
                  "."+str(switchs[n].ip.ip_3))  
            
            for i in range(len(lower_pod_tables)):
                '''
                print("      "+str(lower_pod_tables[i].SuffixTable.SwitchAdress.ip_0)+
                      "."+str(lower_pod_tables[i].SuffixTable.SwitchAdress.ip_1)+
                      "."+str(lower_pod_tables[i].SuffixTable.SwitchAdress.ip_2)+
                      "."+str(lower_pod_tables[i].SuffixTable.SwitchAdress.ip_3)+
                      " |  "+str(lower_pod_tables[i].SuffixTable.suffix.ip_0)+
                      "."+str(lower_pod_tables[i].SuffixTable.suffix.ip_1)+
                      "."+str(lower_pod_tables[i].SuffixTable.suffix.ip_2)+
                      "."+str(lower_pod_tables[i].SuffixTable.suffix.ip_3)+
                      " | "+str(lower_pod_tables[i].SuffixTable.port))
                print(lower_pod_tables[i].SuffixTable.SwitchAdress.ip_1)
                '''
                if switchs[n].ip.ip_1 == lower_pod_tables[i].SuffixTable.SwitchAdress.ip_1 \
                and switchs[n].ip.ip_2 == lower_pod_tables[i].SuffixTable.SwitchAdress.ip_2:
                    for m in range(K*4):
                        if switchs[m].ip.ip_2 == lower_pod_tables[i].SuffixTable.port \
                        and switchs[m].ip.ip_1 == lower_pod_tables[i].SuffixTable.SwitchAdress.ip_1:
                            switchs[m].state = 2
                            print(str(switchs[m].ip.ip_0)+
                                  "."+str(switchs[m].ip.ip_1)+
                                  "."+str(switchs[m].ip.ip_2)+
                                  "."+str(switchs[m].ip.ip_3))
                            return   
Routing_Algorithm()