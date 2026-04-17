
import LectureDonne.optionsArgParse as options
from scapy.all import *
import  LectureDonne.lectureDonneFichierUnique as recupDico  
import LectureDonne.creationCSV as creationCSV
import statistiques.creationRapportStats as stats
import graphiques.creationGraphiques as graphiques


table_par_protocole = recupDico.get_table_par_protocole()

#Selection du scénario en fonction de ce qui est rentré en paramètre
statistique_selectionner = options.get_statistiques()
if statistique_selectionner is not None :
    print ("Statistique sélectionnée : " + statistique_selectionner)
    if statistique_selectionner == "CoucheDeux" :
        print (stats.creationRapport("CoucheDeux",table_par_protocole))
    elif statistique_selectionner == "CoucheTrois" :
        print (stats.creationRapport("CoucheTrois",table_par_protocole))
    elif statistique_selectionner == "CoucheServiceSource" :
        print (stats.creationRapport("CoucheServiceSource",table_par_protocole))
    elif statistique_selectionner == "CoucheServiceDestination" :
         print (stats.creationRapport("CoucheServiceDestination",table_par_protocole))
    elif statistique_selectionner == "TempsVoyage" :
         print (stats.creationRapport("TempsVoyage",table_par_protocole))


elif options.get_rapport() :
    creationCSV.creerCSV(table_par_protocole)


elif options.get_graphique() :
    graphique_selectionner = options.get_graphique()
    print("Mode graphique sélectionné")
    if graphique_selectionner == "CoucheDeux" :
        graphiques.statistiqueSousgraphique(stats.statsCoucheDeux(table_par_protocole),"CoucheDeux")
    elif graphique_selectionner == "CoucheTrois" :
        graphiques.statistiqueSousgraphique(stats.statsCoucheTrois(table_par_protocole),"CoucheTrois")
    elif graphique_selectionner == "CoucheServiceSource" :
        graphiques.statistiqueSousgraphique(stats.statsCoucheServiceSource(table_par_protocole),"CoucheServiceSource")
    elif graphique_selectionner == "CoucheServiceDestination" :
         graphiques.statistiqueSousgraphique(stats.statsCoucheServiceDestination(table_par_protocole),"CoucheServiceDestination")
    elif graphique_selectionner == "TempsVoyage" :
         graphiques.statistiqueTempsVoyageSousgraphique(stats.statsTempsVoyage(table_par_protocole))
else :
    print("Aucun mode n'a été sélectionné, veuillez choisir l'option -s ou -r pour afficher les statistiques ou le rapport CSV" \
    "Pour plus d'informations sur les options disponibles, veuillez utiliser l'option -h ou --help")

#liste chemin du fichier PCAP à analyser
#/home/stagetesa/Downloads/NMAP_PROBE.pcap
