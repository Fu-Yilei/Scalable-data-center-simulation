# -*- coding: utf-8 -*-



#Data center structure simulation for 16 host ports' switch

#The introduction of Fat-Tree
#Structure of End Host

K = 4 #PODS NUMBER


print("\nWe have", K, "Pods")
class IP_Address: #IP Structure
    def __init__(self):
        self.ip_0 = 255   
        self.ip_1 = 255
        self.ip_2 = 255  
        self.ip_3 = 255 
        
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

class Flow_Header:
    def __init__(self):
        self.souce = IP_Address()
        self.destination = IP_Address()
        self.routingresult = []
        self.size = 0
        self.sentport = 0
        self.sentflag = False

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
for i in range(int(K*(K/2)**2)):
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
            _lpt = Routing_table()
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
upper_pod_tables_prefix = []
upper_pod_tables_suffix = []
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
            upper_pod_tables_prefix.append(_upt)
            print("      "+str(_upt.PrefixTable.SwitchAdress.ip_0)+
                  "."+str(_upt.PrefixTable.SwitchAdress.ip_1)+
                  "."+str(_upt.PrefixTable.SwitchAdress.ip_2)+
                  "."+str(_upt.PrefixTable.SwitchAdress.ip_3)+
                  " | "+str(_upt.PrefixTable.prefix.ip_0)+
                  "."+str(_upt.PrefixTable.prefix.ip_1)+
                  "."+str(_upt.PrefixTable.prefix.ip_2)+
                  "."+str(_upt.PrefixTable.prefix.ip_3)+
                  " | "+str(_upt.PrefixTable.port))
        _upt = Routing_table()
        _upt.PrefixTable.SwitchAdress.ip_0 = 10
        _upt.PrefixTable.SwitchAdress.ip_1 = x
        _upt.PrefixTable.SwitchAdress.ip_2 = z
        _upt.PrefixTable.SwitchAdress.ip_3 = 1
        _upt.PrefixTable.prefix.ip_0 = 0
        _upt.PrefixTable.prefix.ip_1 = 0
        _upt.PrefixTable.prefix.ip_2 = 0
        _upt.PrefixTable.prefix.ip_3 = 0
        _upt.PrefixTable.port = 0
        upper_pod_tables_prefix.append(_upt)
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
            upper_pod_tables_suffix.append(_upt)
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

Source_Host_IP_Example = IP_Address()
Source_Host_IP_Example.ip_0 = 10
Source_Host_IP_Example.ip_1 = 0
Source_Host_IP_Example.ip_2 = 1
Source_Host_IP_Example.ip_3 = 2
Destination_Host_IP_Example = IP_Address()
Destination_Host_IP_Example.ip_0 = 10
Destination_Host_IP_Example.ip_1 = 2
Destination_Host_IP_Example.ip_2 = 0
Destination_Host_IP_Example.ip_3 = 3

Routing_Path = []
Port_Path = []
def Step1(Source_Host_IP):
    #Step 1
    for i in range(K*4):
        if switchs[i].ip.ip_1 == Source_Host_IP.ip_1 \
        and switchs[i].ip.ip_2 == Source_Host_IP.ip_2:
            switchs[i].state = 1
            Routing_Path.append(switchs[i])
            Port_Path.append(switchs[i].ip.ip_2)
            print(str(switchs[i].ip.ip_0)+
                  "."+str(switchs[i].ip.ip_1)+
                  "."+str(switchs[i].ip.ip_2)+
                  "."+str(switchs[i].ip.ip_3)+
                  " Port:", switchs[i].ip.ip_2)
            return
    return

#Step 2 
#print(lower_pod_tables[2].SuffixTable.SwitchAdress.ip_2)
def Step2(Destination_Host_IP):
    for n in range(K*4):
        if switchs[n].state == 1:
            for i in range(len(lower_pod_tables)):
                #print(Destination_Host_IP.ip_3 , lower_pod_tables[i].SuffixTable.suffix.ip_3)
                if switchs[n].ip.ip_1 == lower_pod_tables[i].SuffixTable.SwitchAdress.ip_1 \
                and switchs[n].ip.ip_2 == lower_pod_tables[i].SuffixTable.SwitchAdress.ip_2\
                and Destination_Host_IP.ip_3 == lower_pod_tables[i].SuffixTable.suffix.ip_3:
                    for m in range(K*4):
                        if switchs[m].ip.ip_2 == lower_pod_tables[i].SuffixTable.port \
                        and switchs[m].ip.ip_1 == lower_pod_tables[i].SuffixTable.SwitchAdress.ip_1:
                            switchs[m].state = 2
                            Routing_Path.append(switchs[m])
                            Port_Path.append(switchs[i].ip.ip_2)
                            print(str(switchs[m].ip.ip_0)+
                                  "."+str(switchs[m].ip.ip_1)+
                                  "."+str(switchs[m].ip.ip_2)+
                                  "."+str(switchs[m].ip.ip_3)+
                                  " Port:", lower_pod_tables[i].SuffixTable.port)
                            return
    return


#Step3
Skip = 0
def Step3(Destination_Host_IP):
    global Skip
    for n in range(K*4):
        if switchs[n].state == 2:
            for i in range(len(upper_pod_tables_prefix)):                
                if switchs[n].ip.ip_1 == upper_pod_tables_prefix[i].PrefixTable.SwitchAdress.ip_1 \
                and switchs[n].ip.ip_2 == upper_pod_tables_prefix[i].PrefixTable.SwitchAdress.ip_2\
                and Destination_Host_IP.ip_3 == upper_pod_tables_prefix[i].PrefixTable.prefix.ip_3:
                    for p in range(K*4):
                        if switchs[p].ip.ip_1 == Destination_Host_IP.ip_1:
                        #switchs[p].ip.ip_2 == upper_pod_tables_prefix[i].PrefixTable.port \
                        #and switchs[p].ip.ip_1 == upper_pod_tables_prefix[i].PrefixTable.SwitchAdress.ip_1:
                            switchs[p].state = 4
                            '''
                            Routing_Path.append(switchs[p])
                            Port_Path.append(switchs[p].ip.ip_2)
                            print(str(switchs[p].ip.ip_0)+
                                  "."+str(switchs[p].ip.ip_1)+
                                  "."+str(switchs[p].ip.ip_2)+
                                  "."+str(switchs[p].ip.ip_3)+
                                  "Port:", upper_pod_tables_prefix[i].PrefixTable.port)
                            return
                            '''
                            Routing_Path.append(switchs[p])
                            Port_Path.append(switchs[p].ip.ip_2)
                            Skip = 1
                            return
            for i in range(len(upper_pod_tables_suffix)):                
                if switchs[n].ip.ip_1 == upper_pod_tables_suffix[i].SuffixTable.SwitchAdress.ip_1 \
                and switchs[n].ip.ip_2 == upper_pod_tables_suffix[i].SuffixTable.SwitchAdress.ip_2\
                and Destination_Host_IP.ip_3 == upper_pod_tables_suffix[i].SuffixTable.suffix.ip_3:
                    for m in range(int((K/2)**2)):
                        if core_switchs[m].ip.ip_2 == upper_pod_tables_suffix[i].SuffixTable.SwitchAdress.ip_2 -1 \
                        and core_switchs[m].ip.ip_3 == upper_pod_tables_suffix[i].SuffixTable.port -1:           
                            core_switchs[m].state = 3
                            Routing_Path.append(switchs[m])
                            Port_Path.append(switchs[m].ip.ip_2)
                            print(str(core_switchs[m].ip.ip_0)+
                                  "."+str(core_switchs[m].ip.ip_1)+
                                  "."+str(core_switchs[m].ip.ip_2)+
                                  "."+str(core_switchs[m].ip.ip_3)+
                                  " Port:", upper_pod_tables_suffix[i].SuffixTable.port)  
                            return

    return
                           
def Step4(Destination_Host_IP):
    for n in range(int((K/2)**2)):
        if core_switchs[n].state == 3:
            for i in range(len(core_tables)):
                if core_switchs[n].ip.ip_2 == core_tables[i].SwitchAdress.ip_2 \
                and core_switchs[n].ip.ip_3 == core_tables[i].SwitchAdress.ip_3\
                and Destination_Host_IP.ip_1 == core_tables[i].prefix.ip_1:
                    for p in range(K*4):
                        #print(switchs[p].ip.ip_1 )
                        if switchs[p].ip.ip_1 == core_tables[i].port \
                        and switchs[p].ip.ip_2 == core_tables[i].SwitchAdress.ip_2 +1:
                            switchs[p].state = 4
                            Routing_Path.append(switchs[p])
                            Port_Path.append(switchs[p].ip.ip_2)
                            print(str(switchs[p].ip.ip_0)+
                                  "."+str(switchs[p].ip.ip_1)+
                                  "."+str(switchs[p].ip.ip_2)+
                                  "."+str(switchs[p].ip.ip_3)+
                                  " Port:", core_tables[i].port)
                            return   
    return
                    
def Step5(Destination_Host_IP):
    for n in range(K*4):
        if switchs[n].state == 4:
            for i in range(len(upper_pod_tables_suffix)):                
                if switchs[n].ip.ip_1 == upper_pod_tables_suffix[i].SuffixTable.SwitchAdress.ip_1 \
                and switchs[n].ip.ip_2 == upper_pod_tables_suffix[i].SuffixTable.SwitchAdress.ip_2\
                and Destination_Host_IP.ip_3 == upper_pod_tables_suffix[i].SuffixTable.suffix.ip_3\
                and Destination_Host_IP.ip_1 != upper_pod_tables_suffix[i].SuffixTable.SwitchAdress.ip_1:
                    for m in range(int((K/2)**2)):
                        if core_switchs[m].ip.ip_2 == upper_pod_tables_suffix[i].SuffixTable.SwitchAdress.ip_2 -1 \
                        and core_switchs[m].ip.ip_3 == upper_pod_tables_suffix[i].SuffixTable.port -1:                   
                            core_switchs[m].state = 5
                            Routing_Path.append(switchs[m])
                            Port_Path.append(switchs[m].ip.ip_2)
                            print(str(core_switchs[m].ip.ip_0)+
                                  "."+str(core_switchs[m].ip.ip_1)+
                                  "."+str(core_switchs[m].ip.ip_2)+
                                  "."+str(core_switchs[m].ip.ip_3)+
                                  " Port:", upper_pod_tables_suffix[i].SuffixTable.port)  
                            return
                            
            for i in range(len(upper_pod_tables_prefix)):                
                if switchs[n].ip.ip_1 == upper_pod_tables_prefix[i].PrefixTable.SwitchAdress.ip_1 \
                and switchs[n].ip.ip_2 == upper_pod_tables_prefix[i].PrefixTable.SwitchAdress.ip_2\
                and Destination_Host_IP.ip_2 == upper_pod_tables_prefix[i].PrefixTable.prefix.ip_2:
                    for p in range(K*4):
                        if switchs[p].ip.ip_2 == upper_pod_tables_prefix[i].PrefixTable.port \
                        and switchs[p].ip.ip_1 == upper_pod_tables_prefix[i].PrefixTable.SwitchAdress.ip_1:
                            switchs[p].state = 5
                            Routing_Path.append(switchs[p])
                            Port_Path.append(switchs[p].ip.ip_2)
                            print(str(switchs[p].ip.ip_0)+
                                  "."+str(switchs[p].ip.ip_1)+
                                  "."+str(switchs[p].ip.ip_2)+
                                  "."+str(switchs[p].ip.ip_3)+
                                  " Port:", upper_pod_tables_prefix[i].PrefixTable.port)
                            return
    return


def Routing_Algorithm(Source_Host_IP,Destination_Host_IP):
    global Port_Path
    global Routing_Path
    global Skip
    print("Source_Host_IP: "+str(Source_Host_IP.ip_0)+
      "."+str(Source_Host_IP.ip_1)+
      "."+str(Source_Host_IP.ip_2)+
      "."+str(Source_Host_IP.ip_3)+
      " Destination_Host_IP: "+
      str(Destination_Host_IP.ip_0)+
      "."+str(Destination_Host_IP.ip_1)+
      "."+str(Destination_Host_IP.ip_2)+
      "."+str(Destination_Host_IP.ip_3))
    print("Switches passed by:")  
    Step1(Source_Host_IP)
    Step2(Destination_Host_IP)
    Step3(Destination_Host_IP)
    if Skip == 1:
        Step5(Destination_Host_IP)
        Skip = 0
    else:
        Step4(Destination_Host_IP)
        Step5(Destination_Host_IP)
    temp1 = Routing_Path
    temp2 = Port_Path
    Port_Path = []
    Routing_Path = []
    return temp1, temp2


Routing_Algorithm(Source_Host_IP_Example,Destination_Host_IP_Example)

#=============================Flow classification============================================
seen_list = []
_fh1 = Flow_Header()
_fh1.souce = Source_Host_IP_Example
_fh1.destination = Destination_Host_IP_Example
_fh1.routingresult = Routing_Algorithm(_fh1.souce, _fh1.destination)
seen_list.append(_fh1)
_fh_manual = Flow_Header()
def Have_Seen(_fh):
    for i in range(len(seen_list)):
        if _fh.souce.ip_0 == _fh1.souce.ip_0\
        and _fh.souce.ip_1 == _fh1.souce.ip_1\
        and _fh.souce.ip_2 == _fh1.souce.ip_2\
        and _fh.souce.ip_3 == _fh1.souce.ip_3\
        and _fh.destination.ip_0 == _fh1.destination.ip_0\
        and _fh.destination.ip_1 == _fh1.destination.ip_1\
        and _fh.destination.ip_2 == _fh1.destination.ip_2\
        and _fh.destination.ip_3 == _fh1.destination.ip_3:
            return seen_list[i]
    return 0
    
Example_Max_Port_Weight = 50
Example_Min_Port_Weight = 20
Example_Max_Port = 0
Example_Min_Port = 1
    
Incoming_list = [_fh1]
print("Enter the number of packets:")
flow_num = int(input())
for i in range(flow_num):
    _fh = Flow_Header()
    print("Enter Souce IP:")
    souceip = input().split(".")
    print("Enter Destination IP:")
    destinationip = input().split(".")
    _fh.souce.ip_0 = int(souceip[0])
    _fh.souce.ip_1 = int(souceip[1])
    _fh.souce.ip_2 = int(souceip[2])
    _fh.souce.ip_3 = int(souceip[3])
    _fh.destination.ip_0 = int(destinationip[0])
    _fh.destination.ip_1 = int(destinationip[1])
    _fh.destination.ip_2 = int(destinationip[2])
    _fh.destination.ip_3 = int(destinationip[3])
    print("Enter port:")
    _fh.sentport = int(input())
    print("Enter flow weight:")
    _fh.size = int(input())
    
    
for i in range(len(Incoming_list)):
    if Have_Seen(Incoming_list[i]):
        print("We find a match!")
        Incoming_list[i].routingresult = Have_Seen(Incoming_list[i]).routingresult
        Incoming_list[i].sentflag = True
    else:
        Incoming_list[i].routingresult = Routing_Algorithm(Incoming_list[i].souce, Incoming_list[i].destination)
        seen_list.append(Incoming_list[i])
        Incoming_list[i].sentflag = True
End_flag = False
for i in range(0,3):
    D = Example_Max_Port_Weight - Example_Min_Port_Weight
    for j in range(len(Incoming_list)):
        if Incoming_list[j].size <= D:
            Incoming_list[j].sentport = Example_Min_Port
            print("rearranged! Original Port is:", Example_Max_Port, "New Port is:",Incoming_list[j].sentport)
            End_flag = True
            break
    if End_flag == True:
        break
    
'''Test Data
2
10.0.1.2
10.2.0.3
0
10
10.0.1.3
10.2.1.3
0
10
'''







 