
import LectureDonne.optionsArgParse as options
from scapy.all import *
import  LectureDonne.lectureDonneFichierUnique as recupDico  
import statistiques.creationRapportStats as stats


table_par_protocole = recupDico.get_table_par_protocole()

#print (stats.creationRapport("CoucheTrois", table_par_protocole))
print (stats.statsTempsVoyage(table_par_protocole))