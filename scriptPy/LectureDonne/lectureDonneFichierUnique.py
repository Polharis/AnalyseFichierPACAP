import sys
import os

# Remonte d'un niveau pour atteindre la racine du projet
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scapy.all import *
import scriptPy.LectureDonne.trieDeDonnees as trieDeDonnees
import scriptPy.LectureDonne.optionsArgParse as optionsArgParse
import scriptPy.filtrageDonnee.listeFiltre as filtre  


def lancer_lecture_donne_fichier_unique():
    #Récupération de l'emplacement du fichier si il y en a un
    emplacement_fichier = optionsArgParse.get_emplacement_fichier()

    # Récupération du fichier pcapng dans la variable PCAP
    PACAP = rdpcap(emplacement_fichier)
    longueur_PCAP = len(PACAP)

    #Récupération de la plage de temps entrée en paramètre par l'utilisateur
    plage_temps = optionsArgParse.get_plage_temps()


    #Table contenant tous les paquets
    table_par_protocole = {}
    filtres_actives = filtre.liste_filtre_EstActive()

    for (i) in range (0,longueur_PCAP):
        print("chargement" + str(i) + "/" + str(longueur_PCAP), end="\r")
        #Au cas où le paquet n'aurait pas de couche Ethernet, on ne le traite pas (pour éviter la casse du programme)
        if PACAP[i].haslayer(Ether) :
            
            
            table_par_protocole = trieDeDonnees.ajouter_a_table_Par_Protocole(table_par_protocole, PACAP[i], i + 1, filtres_actives)

    return table_par_protocole, plage_temps

def get_table_par_protocole() :
    infos_PCAP = lancer_lecture_donne_fichier_unique()
    table_par_protocole = infos_PCAP[0]
    plage_temps = infos_PCAP[1]
    table_triee = trieDeDonnees.reunir_paquet_par_temps(table_par_protocole, plage_temps)
    
    return table_triee



#Print de test
#print(tableParProtocole.values())








