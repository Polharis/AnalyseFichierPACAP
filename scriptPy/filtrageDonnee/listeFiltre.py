import sys
import os

# Remonte d'un niveau pour atteindre la racine du projet
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import scriptPy.LectureDonne.optionsArgParse as options
import ipaddress

def filtre_Selectionner() :
    filtre = options.get_filtre()
    return filtre

def filtre_ipOnly_EstActive() : 
    if filtre_Selectionner() == "ip_only" :
        return True
    return False

def filtre_arpOnly_EstActive() :
    if filtre_Selectionner() == "arp_only" :
        return True
    return False

def filtre_ipSpecifique_EstActive() :
    filtre = filtre_Selectionner()
    estUneip = True
    try:
        #Si on ne peut pas utiliser ip_address, c'est que le filtre n'est pas une adresse IP
        ipaddress.ip_address(filtre)

    except ValueError:

        estUneip = False

    if filtre is not None and estUneip: #Vérifie que le filtre ressemble à une adresse IP
        return True
    return False

def filtre_portSpecifique_EstActive() :
    filtre = filtre_Selectionner()
    estUnPort = True
    if filtre is None :
        return False
    try:
        #Si on ne peut pas convertir le filtre en int, ce n'est pas un port
        filtre = int(filtre)

    except ValueError:

        estUnPort = False

    if estUnPort: #Vérifie que le filtre ressemble à un port
        if filtre >= 0 and filtre <= 65535 : #Vérifie que le port est dans la plage valide
            return True
    return False



def filtre_protocoleSpecifique_EstActive() :
    filtre = filtre_Selectionner()
    protocoles_ip = ['TCP', 'UDP', 'SCTP', 'ICMP', 'ICMPv6']
    if filtre in protocoles_ip :
        return True
    return False

def liste_filtre_EstActive() :
    filtres = {}
    if filtre_ipOnly_EstActive() :
        filtres["ip_only"] = True
    else : 
        filtres["ip_only"] = False

    if filtre_arpOnly_EstActive() :
        filtres["arp_only"] = True
    else :
        filtres["arp_only"] = False

    if filtre_ipSpecifique_EstActive() :
        filtres["ip_specifique"] = filtre_Selectionner()
    else :
        filtres["ip_specifique"] = None

    if filtre_portSpecifique_EstActive() :
        filtres["port_specifique"] = int(filtre_Selectionner())
    else :
        filtres["port_specifique"] = None

    if filtre_protocoleSpecifique_EstActive() :
        filtres["protocole_specifique"] = filtre_Selectionner()
    else :
        filtres["protocole_specifique"] = None
        
    return filtres