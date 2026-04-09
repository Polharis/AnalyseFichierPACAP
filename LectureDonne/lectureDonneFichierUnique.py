from scapy.all import *
from fonctionsSeparationSelonProtocoleEthernet import *


# Récupération du fichier pcapng dans la varaible PCAP
PACAP = rdpcap("/home/stagetesa/projet git/AnalyseFichierPACAP/DataEntry/exempleCaptureWireshark.pcapng")
longueurPCAP = len(PACAP)

#Traitement de ces fichiers pour ne garder que les informations qui nous intéressent


#table contenant tout les paquet
tableParProtocole = {}


for (i) in range (0,longueurPCAP):
    tableParProtocole = ajouterATableParProtocole(tableParProtocole, PACAP[i])

def getTableParProtocole() :
    return tableParProtocole
#print(tableParProtocole.values())
#print(PACAP[40].show())


