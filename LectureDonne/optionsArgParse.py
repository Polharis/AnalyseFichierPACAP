import argparse
import os

FICHIER_PCAP_DEFAUT = "DataEntry/exempleCaptureWireshark.pcapng"

def ajouter_parser():
    #Ajout d'options pour avoir des fonctionnalités supplémentaires
    parser = argparse.ArgumentParser(description="Analyse d'un fichier pcapng")
    #Option permettant de choisir un fichier PCAP en dehors du projet
    parser.add_argument("-f", "--fichier", help="Le chemin du fichier pcapng à analyser", required=False)
    #Option pour regrouper des paquets identiques sur une plage de temps donnée
    parser.add_argument("-p", "--plage-temps", help="La plage de temps à analyser (format: 'nbSecondes)", required=False)
    #Option pour n'afficher que les paquet de type IP ou IPV6
    parser.add_argument("-filtre", "--filtre", help="Applique un filtre sur l'analyse des paquets." \
                                                    "   Voicie la liste des filtre disponibles:" \
                                                    "   'ip_only' : N'affiche que les paquets de type IP ou IPv6 |" \
                                                    "   'arp_only' : N'affiche que les paquets de type ARP |" \
                                                    "   une ip ex : '192.168.1.1' : N'affiche que les paquets provenant ou étant déstiné à de cette adresse IP |" \
                                                    "", required=False)

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

def get_emplacement_fichier():
    args = ajouter_parser()
    if args.fichier is None :
        return FICHIER_PCAP_DEFAUT
    else : 

        fichier = args.fichier

        if(len(fichier)) > 0 :
            #Permet de vérifier si on tombe sur une erreur du type : FileNotFoundError
            #Vérifie aussi si le paramètre n'est pas un broken symbolic links comme un int pas exemple
            if not os.path.isfile(fichier):
                print("Erreur, le chemin spécifier en paramètre est incorrecte, " \
                      "le fichier PCAP par défaut à été sélectionné")
                return FICHIER_PCAP_DEFAUT
                
            return fichier
            
        print("Erreur: chemin non adapté, le fichier PCAP par défaut à été sélectionné")
        return FICHIER_PCAP_DEFAUT
    
def get_filtre():
    args = ajouter_parser()
    return args.filtre
    