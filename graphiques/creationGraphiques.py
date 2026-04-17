import matplotlib.pyplot as plt
import pandas as pd


def statistiqueSousgraphique(stats_table, graph_type) : 
    #Cette fonction prend en entrée une table de statistiques et retourne un graphique 
    # Réaliser avec panda se servant de matplotlib pour faire le graphique
    stats_table.pop("total_paquet", None)
    graph = pd.Series(stats_table)
    graph.plot(kind="pie", autopct='%1.1f%%')
    if graph_type == "CoucheServiceDestination" or graph_type == "CoucheServiceSource" :
        information = "services"
    else : 
        information = "protocoles"

    plt.title("Graphique des statistiques de la " + graph_type)
    plt.xlabel(information)
    plt.ylabel("Pourcentage de paquets")
    plt.tight_layout()
    plt.show()

def statistiqueTempsVoyageSousgraphique(stats_table) : 
    #Cette fonction prend en entrée une table de statistiques et retourne un graphique 
    # Réaliser avec panda se servant de matplotlib pour faire le graphique
    graph = pd.Series(stats_table[0])
    graph.plot(kind="bar")
    plt.title("Graphique moyenne de temps pris pour les aller-retour entre les différentes conversations")
    plt.xlabel("Conversations")
    plt.ylabel("Moyenne du temps de voyage (en secondes)")
    plt.tight_layout()
    plt.show()