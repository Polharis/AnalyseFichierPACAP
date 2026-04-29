import sys
import os
import socket

# Remonte d'un niveau pour atteindre la racine du projet
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import dpkt
from scapy.all import *
import scriptPy.LectureDonne.trieDeDonnees as trieDeDonnees
import scriptPy.LectureDonne.optionsArgParse as optionsArgParse
import scriptPy.filtrageDonnee.listeFiltre as filtre  


cache = {'table': None, 'plage_temps': None,'filtres': None,'emplacement_fichier': None, "plage_temps_graph": None,'initialized': False}

def lancer_lecture_donne_fichier_unique():

    #Récupération de la plage de temps entrée en paramètre par l'utilisateur
    plage_temps = optionsArgParse.get_plage_temps()

    

    filtres_actives = filtre.liste_filtre_EstActive()

    plage_temps_graphique = optionsArgParse.get_plage_temps_graphique()

    #Récupération de l'emplacement du fichier si il y en a un
    emplacement_fichier = optionsArgParse.get_emplacement_fichier()

    #-------------------------- TEST DPKT ------------------------

    

       
         
    #---------------------------------------------------------------
    

    #Vérification si les données ont déjà été traitées pour éviter de les retraiter à chaque fois
    if cache['initialized'] and cache['emplacement_fichier'] == emplacement_fichier and cache['filtres'] == filtres_actives and cache['plage_temps'] == plage_temps and cache['plage_temps_graph'] == plage_temps_graphique:
        return cache['table'], plage_temps

    

    # Récupération du fichier pcapng ou pcap
    with open(emplacement_fichier, 'rb') as f:
        magic = f.read(4)
        f.seek(0)  # rewind

        # Détection automatique du format
        if magic == b'\x0a\x0d\x0d\x0a':
            reader = dpkt.pcapng.Reader(f)
        else:
            reader = dpkt.pcap.Reader(f)

        #Table contenant tous les paquets
        table_par_protocole = {}
        i = 0

        for ts, buf in reader:
            if i % 1000 == 0:  
                print("chargement " + str(i) + " paquets lus")
            
            # Vérifier que c'est bien une couche Ethernet valide
            try:
                eth = dpkt.ethernet.Ethernet(buf)
                print(buf)
                if isinstance(eth, dpkt.ethernet.Ethernet):
                    table_par_protocole = trieDeDonnees.ajouter_a_table_Par_Protocole(table_par_protocole, eth, i + 1, filtres_actives)
            except:
                # Ignorer les paquets qui ne peuvent pas être parsés
            
                pass
            
            i += 1

    cache['table'] = table_par_protocole
    cache['initialized'] = True
    cache['filtres'] = filtres_actives
    cache['emplacement_fichier'] = emplacement_fichier
    cache['plage_temps'] = plage_temps
    cache['plage_temps_graph'] = plage_temps_graphique
    print (table_par_protocole)
    return table_par_protocole, plage_temps

def get_table_par_protocole() :
    infos_PCAP = lancer_lecture_donne_fichier_unique()
    table_par_protocole = infos_PCAP[0]
    plage_temps = infos_PCAP[1]
    table_triee = trieDeDonnees.reunir_paquet_par_temps(table_par_protocole, plage_temps)
    
    return table_triee



#Print de test
#print(tableParProtocole.values())








