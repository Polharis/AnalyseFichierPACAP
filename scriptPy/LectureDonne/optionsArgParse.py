import argparse
import os

# Chemin par défaut relatif à la location de ce fichier
FICHIER_PCAP_DEFAUT = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..",
    "DataEntry",
    "exempleCaptureWireshark.pcapng"
)
filtres_à_appliquer = {}

def appliquer_filtres(params):
    print("Application des filtres : ", params)
    print(params["port_specifique"])
    #Ici on applique les filtres en fonction des paramètres reçus
    for key, value in params.items():
        filtres_à_appliquer[key] = value

def get_plage_temps():
    
    return None

def get_emplacement_fichier():
  
    return FICHIER_PCAP_DEFAUT
   
    
def get_filtre():
    args = filtres_à_appliquer
    
    return args




