import sys
import os

# Remonte d'un niveau pour atteindre la racine du projet
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import scriptPy.LectureDonne.optionsArgParse as options
from scapy.all import *
import  scriptPy.LectureDonne.lectureDonneFichierUnique as recupDico  

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

def liste_différence_src_dst_adjacente(dicoReseau) :
    src_dst = {}
    src_dst_diff = {}
    for key in dicoReseau.keys() :
        for paquet in dicoReseau[key] :
            if "source" in paquet.keys() and "destination" in paquet.keys() :
                src_dst.setdefault((paquet["source"],paquet["destination"]),[]).append(paquet["time"])
    for couple in src_dst.keys() :
        liste_difference = []
        src_dst[couple].sort()
        for i in range (len(src_dst[couple])) :
            if i == len(src_dst[couple]) -1 :
                break
            if i % 2 == 0 :
                n = src_dst[couple][i].timestamp() * 1000 #en millisecondes
                n_plus_un = src_dst[couple][i+1].timestamp() * 1000 #en millisecondes
                liste_difference.append(n_plus_un - n)
        src_dst_diff.setdefault(couple,liste_difference)
    return src_dst_diff

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

    # Ce mode n'est pas pertinant, a ne pas  utiliser pour le moment, mais je le laisse au cas où je voudrais faire des analyses plus poussées sur les temps de voyage des paquets
    if mode == "TempsVoyageMoyen" :
        rapport += "Statistque sur le temps de voyage des paquets\n"
        stats = statsTempsVoyageMoyen(table)
        tars_moyens = stats[0]
        nb_tars = stats[1]
        if not tars_moyens :
            rapport += "Aucune paire de paquets aller-retour n'a été trouvée pour calculer les temps de voyage moyens.\n"
        else : 
            for conversation in tars_moyens.keys() :
                
                rapport += (
                    "Conversation entre " + conversation[0] + " et " + conversation[1] +
                    " : TAR moyen de " + str(tars_moyens[conversation]) + " secondes, basé sur " +
                    str(nb_tars[conversation]) + " paires aller-retour\n"
                )

    return rapport








#----------------------------------------------------------------------------------------------------
# ----------------------- A mettre entre parenthèse car je n'ai pas tout les outils -----------------


#Liste des temps de voyage pour chaque conversation (src, dst) 
# pour de futures analyses plus poussées sur les temps de voyage (ex : distribution des temps de voyage, etc...)
def dicoTempsParConversation(dicoReseau) :
    # Collecte des temps par conversation (src, dst)
    conversations = {}  # clé: (src, dst), valeur: liste des temps
    for protocoles_couches_1 in dicoReseau.keys() : 
        for paquet in dicoReseau[protocoles_couches_1] : 
            if "source" in paquet.keys() and "destination" in paquet.keys() : 
                key = (paquet["source"], paquet["destination"])
                # setDefault très pratique car évite de devoir vérifier si la clé existe déjà ou pas
                conversations.setdefault(key, []).append(paquet["time"])
    return conversations

#fait la moyenne du temps mis par chaque packet pout voyager entre la source et la destination
#Permet aussi d'obtenir le nombre de paires aller-retour pour chaque conversation (src, dst) 
# pour pouvoir faire des statistiques plus précises sur les temps de voyage moyens

def statsTempsVoyageMoyen(dicoReseau) :

    #Liste des conversations (src, dst) avec les temps de chaque paquet pour chaque conversation
    conversations = dicoTempsParConversation(dicoReseau)

    # Calcule des TAR (temps aller retour)moyens pour chaque paire
    tars_moyens = {}
    nb_tars = {}
    for (src, dst), times_out in conversations.items():
        #On récupère le temps du couple inverse (dst, src) pour trouver les temps de retour
        times_back = conversations.get((dst, src), [])
        if times_back:
            # Trie les temps
            times_out.sort()
            times_back.sort()
            # Calcule les différences pour les paires (aller-retour)
            num_pairs = min(len(times_out), len(times_back))
            diffs = []
            for i in range(num_pairs):
                diff = times_back[i] - times_out[i]
                if diff.total_seconds() > 0:
                    diffs.append(diff.total_seconds())
                    nb_tars[(src, dst)] = i +1
            if diffs:
                avg_rtt = sum(diffs) / len(diffs)
                tars_moyens[(src, dst)] = avg_rtt
                

    return [tars_moyens,nb_tars,conversations]

def statsTempsVoyageUnitaire(dicoReseau) : 

    #Liste des conversations (src, dst) avec les temps de chaque paquet pour chaque conversation
    conversations = dicoTempsParConversation(dicoReseau)

    tars_unitaires = {}
    for (src, dst), times_out in conversations.items():
        #On récupère le temps du couple inverse (dst, src) pour trouver les temps de retour
        times_back = conversations.get((dst, src), [])
        if times_back:
            # Trie les temps
            times_out.sort()
            times_back.sort()
            # Calcule les différences pour les paires (aller-retour)
            num_pairs = min(len(times_out), len(times_back))
            for i in range(num_pairs):
                diff = times_back[i] - times_out[i]
                if diff.total_seconds() > 0:
                    tars_unitaires.setdefault((src,dst),[]).append(diff.total_seconds())

    return tars_unitaires


