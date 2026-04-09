import argparse

def ajouterParser():
    parser = argparse.ArgumentParser(description="Analyse d'un fichier pcapng")
    parser.add_argument("-f", "--fichier", help="Le chemin du fichier pcapng à analyser", required=False)
    parser.add_argument("-p", "--plage-temps", help="La plage de temps à analyser (format: 'HH:MM:SS-AAAA:MM:JJ')", required=False)
    return parser.parse_args()





def getPlageTemps():
    args = ajouterParser()
    tempsEnString = str(args.plage_temps)
    if args.plage_temps:
        if tempsEnString[2] == ":" and tempsEnString[5] == ":" and tempsEnString[8] == "-" and tempsEnString[13] == ":" and tempsEnString[16] == ":" :
            return args.plage_temps
    return None