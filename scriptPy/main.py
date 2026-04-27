import LectureDonne.optionsArgParse as options
from scapy.all import *
import  LectureDonne.lectureDonneFichierUnique as recupDico  
import LectureDonne.creationCSV as creationCSV
import statistiques.creationRapportStats as stats
import graphiques.creationGraphiques as graphiques







def genererGraphique(TypeGraphique,plage_temps_graphique) :
    table_par_protocole = recupDico.get_table_par_protocole()
    
    if TypeGraphique == "CoucheDeux" :
        return graphiques.statistiqueSousgraphique(stats.statsCoucheDeux(table_par_protocole),"EtherType")
    elif TypeGraphique == "CoucheTrois" :
        return graphiques.statistiqueSousgraphique(stats.statsCoucheTrois(table_par_protocole),"CoucheTrois")
    elif TypeGraphique == "CoucheQuatre" :
        return graphiques.statistiqueSousgraphique(stats.statsCoucheQuatre(table_par_protocole),"CoucheQuatre")
    elif TypeGraphique == "CoucheServiceSource" :
        return graphiques.statistiqueSousgraphique(stats.statsCoucheServiceSource(table_par_protocole),"CoucheServiceSource")
    elif TypeGraphique == "CoucheServiceDestination" :
         return graphiques.statistiqueSousgraphique(stats.statsCoucheServiceDestination(table_par_protocole),"CoucheServiceDestination")
    elif TypeGraphique == "IntraEspacement" :
        return graphiques.histogrammeIntraEspacement(stats.liste_différence_src_dst_adjacente(table_par_protocole,plage_temps_graphique),plage_temps_graphique)
    elif TypeGraphique == "IntraEspacementRepartition" :
        return graphiques.courbeRepartitionIntraEspacement(stats.liste_différence_src_dst_adjacente(table_par_protocole,plage_temps_graphique),plage_temps_graphique)
    else :
        return None

def genererRapportCsv() :
    table_par_protocole = recupDico.get_table_par_protocole()
    creationCSV.creationCSVtoutesInfos(table_par_protocole)

def genererRapportStatistique(mode) :
    table_par_protocole = recupDico.get_table_par_protocole()
    if mode == "CoucheDeux" :
        return stats.creationRapport(mode,table_par_protocole)
    elif mode == "CoucheTrois" :
        return stats.creationRapport(mode,table_par_protocole)
    elif mode == "CoucheServiceSource" :    
        return stats.creationRapport(mode,table_par_protocole)
    elif mode == "CoucheServiceDestination" :
        return stats.creationRapport(mode,table_par_protocole)
    else :
        return None


#liste chemin du fichier PCAP à analyser
#/home/stagetesa/Downloads/NMAP_PROBE.pcap