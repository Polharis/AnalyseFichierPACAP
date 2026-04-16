import sys
import os

# Remonte d'un niveau pour atteindre la racine du projet
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import LectureDonne.optionsArgParse as options
from scapy.all import *
import  LectureDonne.lectureDonneFichierUnique as recupDico  

def statsCoucheDeux(dicoReseau):
    #On compte le nombre de paquets de chaque type de protocole de couche 2
    stats = {}
    for protocols_couches_1 in dicoReseau.keys() : 
        stats[protocols_couches_1] = len(dicoReseau[protocols_couches_1])
    stats_pourcentage = {}
    total_paquet = 0
    for listes_paquets in dicoReseau.values() :
        total_paquet += len(listes_paquets)
    stats_pourcentage["total_paquet"] = total_paquet
    for protos in stats.keys() :
        stats_pourcentage[protos] = (stats[protos] / total_paquet) * 100

    return stats_pourcentage

def statsCoucheTrois(dicoReseau) :
    #On compte le nombre de paquets de chaque type de protocole de couche 3
    stats = {}
    for protocols_couches_1 in dicoReseau.keys() : 
        for paquet in dicoReseau[protocols_couches_1] :
            if 'protocole_3' in paquet.keys() :
                proto_couche_3 = paquet['protocole_3']
                if proto_couche_3 not in stats.keys() :
                    stats[proto_couche_3] = 1
                else :
                    stats[proto_couche_3] += 1
    stats_pourcentage = {}
    total_paquet = 0
    for listes_paquets in dicoReseau.values() :
        total_paquet += len(listes_paquets)
    stats_pourcentage["total_paquet"] = total_paquet
    for protos in stats.keys() :
        stats_pourcentage[protos] = (stats[protos] / total_paquet) * 100

    return stats_pourcentage

def statsCoucheServiceSource(dicoReseau) :
    stats = {}
    for protocols_couches_1 in dicoReseau.keys() : 
        for paquet in dicoReseau[protocols_couches_1] :
            if 'port_src' in paquet.keys() :
                service = paquet['port_src']
                if service not in stats.keys() :
                    stats[service] = 1
                else :
                    stats[service] += 1
    stats_pourcentage = {}
    total_paquet = 0
    for listes_paquets in dicoReseau.values() :
        total_paquet += len(listes_paquets)
    stats_pourcentage["total_paquet"] = total_paquet
    for protos in stats.keys() :
        stats_pourcentage[protos] = (stats[protos] / total_paquet) * 100
    return stats_pourcentage    

def statsCoucheServiceDestination(dicoReseau) :
    stats = {}
    for protocols_couches_1 in dicoReseau.keys() : 
        for paquet in dicoReseau[protocols_couches_1] :
            if 'port_dst' in paquet.keys() :
                service = paquet['port_dst']
                if service not in stats.keys() :
                    stats[service] = 1
                else :
                    stats[service] += 1
    stats_pourcentage = {}
    total_paquet = 0
    for listes_paquets in dicoReseau.values() :
        total_paquet += len(listes_paquets)
    stats_pourcentage["total_paquet"] = total_paquet
    for protos in stats.keys() :
        stats_pourcentage[protos] = (stats[protos] / total_paquet) * 100
    return stats_pourcentage    


def creationRapport(mode,table) :
    rapport = ""
    if mode == "CoucheDeux" : 
        rapport += "Statistque sur la deuxième couche\n"
        stats = statsCoucheDeux(table)
        for stat in stats.keys() : 
            if stat == "total_paquet" :
                rapport += "Nombre total de paquets traités : " + str(stats[stat]) + "\n"
            else :
                rapport += " protocols : " + stat + " présents à " + str(stats[stat]) + "%\n"
    if mode == "CoucheTrois" :
        rapport += "Statistque sur la troisième couche\n"
        stats = statsCoucheTrois(table)
        for stat in stats.keys() : 
            if stat == "total_paquet" :
                rapport += "Nombre total de paquets traités : " + str(stats[stat]) + "\n"
            else :
                rapport += " protocols : " + stat + " présents à " + str(stats[stat]) + " %\n"
    if mode == "CoucheServiceSource" :
        rapport += "Statistque sur les services sources\n"
        stats = statsCoucheServiceSource(table)
        for stat in stats.keys() : 
            if stat == "total_paquet" :
                rapport += "Nombre total de paquets traités : " + str(stats[stat]) + "\n"
            else :
                rapport += " service : " + stat + " présents à " + str(stats[stat]) + " %\n"
    if mode == "CoucheServiceDestination" :
        rapport += "Statistque sur les services destinations\n"
        stats = statsCoucheServiceDestination(table)
        for stat in stats.keys() : 
            if stat == "total_paquet" :
                rapport += "Nombre total de paquets traités : " + str(stats[stat]) + "\n"
            else :
                rapport += " service : " + stat + " présents à " + str(stats[stat]) + " %\n"

    return rapport


