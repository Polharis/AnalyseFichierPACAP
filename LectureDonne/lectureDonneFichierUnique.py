from scapy.all import *
from fonctionsSeparationSelonProtocoleEthernet import *

# Récupération du fichier pcapng dans la varaible PCAP
PACAP = rdpcap("/home/stagetesa/projet git/AnalyseFichierPACAP/DataEntry/exempleCaptureWireshark.pcapng")
longueurPCAP = len(PACAP)

#Traitement de ces fichiers pour ne garder que les informations qui nous intéressent



#Une liste par protocole existant
PACAPIPV4 = [["numeroPacket"],["IPSource"],["IPDestination"],["ttl"],["longueur"],["timeStamp"]]
PCAPARP= [["numeroPacket"],["IPSource"],["IPDestination"],["ttl"],["longueur"],["timeStamp"]]
PACAPIPV6 = [["numeroPacket"],["IPSource"],["IPDestination"],["ttl"],["longueur"],["timeStamp"]]
PCAPVLAN8021Q = [["numeroPacket"],["IPSource"],["IPDestination"],["ttl"],["longueur"],["timeStamp"]]
PCAPMPLS = [["numeroPacket"],["IPSource"],["IPDestination"],["ttl"],["longueur"],["timeStamp"]]
PCAPLLDP = [["numeroPacket"],["IPSource"],["IPDestination"],["ttl"],["longueur"],["timeStamp"]]
PCAPWakeOnLan = [["numeroPacket"],["IPSource"],["IPDestination"],['ttl'],['longueur'],['timeStamp']]

for (i) in range (0,longueurPCAP):
    if PACAP[i][Ether].payload.name == "ARP":
        ajoutePaquetARP(PACAP[i],i,PCAPARP)
    if PACAP[i][Ether].payload.name == "IP":
        ajoutePaquetIP(PACAP[i],i,PACAPIPV4)
    if PACAP[i][Ether].payload.name == "IPv6":
        ajoutePaquetIPv6(PACAP[i],i,PACAPIPV6)
    if PACAP[i][Ether].payload.name == "802.1Q":
        ajoutePaquetVLAN8021Q (PACAP[i],i,PCAPVLAN8021Q)
    if PACAP[i][Ether].payload.name == "MPLS unicast":
        ajoutePaquetMPLS(PACAP[i],i,PCAPMPLS)
    if PACAP[i][Ether].payload.name == "MPLS multicast":
        ajoutePaquetMPLS(PACAP[i],i,PCAPMPLS)
    if PACAP[i][Ether].payload.name == "LLDP":
        ajoutePaquetLLDP(PACAP[i],i,PCAPLLDP)
    if PACAP[i][Ether].payload.name == "Wake on LAN":
        ajoutePaquetWakeOnLan(PACAP[i],i)

print (PCAPMPLS)



