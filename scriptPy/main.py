import LectureDonne.optionsArgParse as options
from scapy.all import *
import  LectureDonne.lectureDonneFichierUnique as recupDico  
import LectureDonne.creationCSV as creationCSV
import statistiques.creationRapportStats as stats
import graphiques.creationGraphiques as graphiques







def genererGraphique(TypeGraphique) :
    table_par_protocole = recupDico.get_table_par_protocole()
    if TypeGraphique == "CoucheDeux" :
        return graphiques.statistiqueSousgraphique(stats.statsCoucheDeux(table_par_protocole),"CoucheDeux")
    elif TypeGraphique == "CoucheTrois" :
        return graphiques.statistiqueSousgraphique(stats.statsCoucheTrois(table_par_protocole),"CoucheTrois")
    elif TypeGraphique == "CoucheServiceSource" :
        return graphiques.statistiqueSousgraphique(stats.statsCoucheServiceSource(table_par_protocole),"CoucheServiceSource")
    elif TypeGraphique == "CoucheServiceDestination" :
         return graphiques.statistiqueSousgraphique(stats.statsCoucheServiceDestination(table_par_protocole),"CoucheServiceDestination")
    elif TypeGraphique == "InterEspacement" :
        return graphiques.histogrammeInterEspacement(stats.liste_différence_src_dst_adjacente(table_par_protocole))
    else :
        return None

def genererRapportCsv() :
    table_par_protocole = recupDico.get_table_par_protocole()
    creationCSV.creationCSVtoutesInfos(table_par_protocole)


#liste chemin du fichier PCAP à analyser
#/home/stagetesa/Downloads/NMAP_PROBE.pcap