import sys
import os

# Remonte d'un niveau pour atteindre la racine du projet
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scapy.all import *
import LectureDonne.trieDeDonnees as trieDeDonnees
import LectureDonne.optionsArgParse as optionsArgParse
import filtrageDonnee.listeFiltre as filtre  



#Récupération de l'emplacement du fichier si il y en a un
emplacement_fichier = optionsArgParse.get_emplacement_fichier()

# Récupération du fichier pcapng dans la variable PCAP
PACAP = rdpcap(emplacement_fichier)
longueur_PCAP = len(PACAP)

#Récupération de la plage de temps entrée en paramètre par l'utilisateur
plage_temps = optionsArgParse.get_plage_temps()


#Table contenant tous les paquets
table_par_protocole = {}


for (i) in range (0,longueur_PCAP):
    #Au cas où le paquet n'aurait pas de couche Ethernet, on ne le traite pas (pour éviter la casse du programme)
    if PACAP[i].haslayer(Ether) :
        filtres_actives = filtre.liste_filtre_EstActive()
        table_par_protocole = trieDeDonnees.ajouter_a_table_Par_Protocole(table_par_protocole, PACAP[i], i + 1, filtres_actives)



def get_table_par_protocole() :
    table_triee = trieDeDonnees.reunir_paquet_par_temps(table_par_protocole, plage_temps)
    
    return table_triee



#Print de test
#print(tableParProtocole.values())

print(PACAP[28].show())





