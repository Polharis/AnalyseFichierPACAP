from scapy.all import *
from lectureDonneFichierUnique import getTableParProtocole
from fonctionsSeparationSelonProtocoleEthernet import *
import csv

#Récupération du dictionnaire contenant les données extraites du fichier pcapng
tableParProtocole = getTableParProtocole()

#Création du fichier csv avec les données extraites du fichier pcapng

#informations de la première colonne du csv
premiereColonne = []
for donnee in tableParProtocole.values() :
    for dico in donnee : 
        for info in dico.keys() :
            if info not in premiereColonne :
                premiereColonne.append(info)

#Toutes les infos
toutesInfos = [['donnees']]
i = 1
for donnee in tableParProtocole.values() :
    for dico in donnee : 
        toutesInfos[0].append("paquet" + str(i))
        i += 1

for (i) in range (0, len(premiereColonne)) :
    toutesInfos.append([])
    toutesInfos[i+1].append(premiereColonne[i])
    for donnee in tableParProtocole.values() :
        for dico in donnee : 
            if premiereColonne[i] not in dico.keys() : 
                toutesInfos[i+1].append("None")
            else :
                toutesInfos[i+1].append(dico[premiereColonne[i]])


# Écrire le CSV
with open('data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for lignes in toutesInfos :
        writer.writerow(lignes)
    
f.close()