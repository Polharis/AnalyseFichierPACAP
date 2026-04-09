from scapy.all import *
from fonctionsSeparationSelonProtocoleEthernet import *
from optionsArgParse import *



# Récupération du fichier pcapng dans la varaible PCAP
PACAP = rdpcap("/home/stagetesa/projet git/AnalyseFichierPACAP/DataEntry/exempleCaptureWireshark.pcapng")
longueurPCAP = len(PACAP)

#récupération de la plage de temps entrer en paramètre par l'utilisateur
PlageTemps = getPlageTemps()

#Traitement de ces fichiers pour ne garder que les informations qui nous intéressent


#table contenant tout les paquet
tableParProtocole = {}


for (i) in range (0,longueurPCAP):
    #au cas où le paquet n'aurait pas de couche Ethernet, on ne le traite pas (pour éviter la casse du programme)
    if PACAP[i].haslayer(Ether) :
        tableParProtocole = ajouterATableParProtocole(tableParProtocole, PACAP[i])

def getTableParProtocole() :
    return tableParProtocole
#print(tableParProtocole.values())
#print(PACAP[40].show())
print(PlageTemps)



