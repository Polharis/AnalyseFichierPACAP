import argparse

def ajouter_parser():
    #Ajout d'options pour avoir des fonctionnalités supplémentaires
    parser = argparse.ArgumentParser(description="Analyse d'un fichier pcapng")
    #Option permettant de choisir un fichier PCAP en dehors du projet
    parser.add_argument("-f", "--fichier", help="Le chemin du fichier pcapng à analyser", required=False)
    #Option pour regrouper des paquets identiques sur une plage de temps donnée
    parser.add_argument("-p", "--plage-temps", help="La plage de temps à analyser (format: 'nbSecondes)", required=False)
    return parser.parse_args()





def get_plage_temps():
    args = ajouter_parser()
    #On vérifie que l'utilisateur a bien utilisé le paramètre -p
    if args.plage_temps is None:
        return None
    #Ici on vérifie que la plage de temps est bien un nombre supérieur à 0
    try:
        temps_en_int = float(args.plage_temps)
        #Pas de temps négatifs
        if temps_en_int > 0.0:
            return temps_en_int
    except ValueError:
        print("Erreur: la plage de temps doit être un nombre entier")
    return None
    