from scapy.all import *
import trieDeDonnees 
import optionsArgParse  



# Récupération du fichier pcapng dans la variable PCAP
PACAP = rdpcap("/home/stagetesa/projet git/AnalyseFichierPACAP/DataEntry/exempleCaptureWireshark.pcapng")
longueur_PCAP = len(PACAP)

#Récupération de la plage de temps entrée en paramètre par l'utilisateur
plage_temps = optionsArgParse.get_plage_temps()


#Table contenant tous les paquets
table_par_protocole = {}


for (i) in range (0,longueur_PCAP):
    #Au cas où le paquet n'aurait pas de couche Ethernet, on ne le traite pas (pour éviter la casse du programme)
    if PACAP[i].haslayer(Ether) :
        table_par_protocole = trieDeDonnees.ajouter_a_table_Par_Protocole(table_par_protocole, PACAP[i], i + 1)



def get_table_par_protocole() :
    table_triee = trieDeDonnees.reunir_paquet_par_temps(table_par_protocole, plage_temps)
    
    return table_triee



#print(tableParProtocole.values())




