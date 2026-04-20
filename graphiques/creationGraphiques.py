import matplotlib.pyplot as plt
import pandas as pd


def statistiqueSousgraphique(stats_table, graph_type) : 
    #Cette fonction prend en entrée une table de statistiques et retourne un graphique 
    # Réaliser avec panda se servant de matplotlib pour faire le graphique
    stats_table.pop("total_paquet", None)
    liste_cle_a_supprimer = []
    for key in stats_table.keys() :
        if stats_table[key] < 0.5 :
            liste_cle_a_supprimer.append(key)
    for key in liste_cle_a_supprimer :
        stats_table.setdefault("Other", 0)
        stats_table["Other"] += stats_table[key]
        stats_table.pop(key, None)

    graph = pd.Series(stats_table)
    graph.plot(kind="pie", autopct='%1.1f%%')
    if graph_type == "CoucheServiceDestination" or graph_type == "CoucheServiceSource" :
        information = "services"
    else : 
        information = "protocoles"

    plt.title("Graphique des statistiques de la " + graph_type)


    plt.xlabel("porcentage de " + information + "sur l'ensemble des paquets")
    plt.tight_layout()
    plt.show()


#Créer un histogramme de l'inter-espacement entre les paquets pour chaque conversation (src, dst)
def histogrammeInterEspacement(dicoReseau) :
    # dicoReseau : { (src, dst): [inter_espacement_ms] }
    histogram_data = []
    labels = []

    for (src, dst), times in dicoReseau.items() :
        if not times :
            continue
        histogram_data.append(times)
        labels.append(f"{src} → {dst}")

    if not histogram_data :
        print("Aucune donnée d'inter-espacement disponible pour tracer un histogramme.")
        return None

    fig, ax = plt.subplots()
    ax.hist(histogram_data, bins=100, label=labels, alpha=0.6, edgecolor='black')
    ax.set_title("Histogramme des inter-espacements par conversation")
    ax.set_xlabel("Inter-espacement (millisecondes)")
    ax.set_ylabel("Nombre d'intervalles")
    ax.legend(loc="best", fontsize="small")
    ax.grid(True)
    plt.tight_layout()
    plt.show()















#----------------------------------------------------------------------------------------------------
# ----------------------- A mettre entre parenthèse car je n'ai pas tout les outils -----------------

def statistiqueTempsVoyageMoyenSousgraphique(stats_table) : 
    #Cette fonction prend en entrée une table de statistiques et retourne un graphique 
    # Réaliser avec panda se servant de matplotlib pour faire le graphique
    graph = pd.Series(stats_table[0])
    graph.plot(kind="bar")
    plt.title("Graphique moyenne de temps pris pour les aller-retour entre les différentes conversations")
    plt.xlabel("Conversations")
    plt.ylabel("Moyenne du temps de voyage (en secondes)")
    plt.tight_layout()
    plt.show()

def statistiqueTempsVoyageUnitaireSousgraphique(table_temps) :
    # table_temps : {(src, dst): [temps]}
    # Pour chaque couple source/destination, on trace la courbe cumulative des temps de voyage unitaire.
    fig, ax = plt.subplots()
    liste_temps = []

    for (src, dst), times in table_temps.items() :
        if not times :
            continue
        liste_temps.append(times)
        max_progressif = pd.Series(liste_temps).cummax()
        ax.plot(
            range(1, len(max_progressif) + 1),
            max_progressif,
            marker='o',
            label=f"{src} → {dst}"
        )

    ax.set_title("Graphique du temps maximum progressif par conversation")
    ax.set_xlabel("Nombre de paquets")
    ax.set_ylabel("Temps maximum trouvé (secondes)")
    ax.legend(loc="best", fontsize="small")
    ax.grid(True)
    plt.tight_layout()
    plt.show()

def statistiqueTempsVoyageRepartitionSousgraphique(table_temps) :
    # table_temps : {(src, dst): [temps]}
    # On trace la répartition des temps de voyage unitaire pour chaque conversation.
    fig, ax = plt.subplots()

    for (src, dst), times in table_temps.items() :
        if not times : 
            continue
        ax.plot(
            range(1, len(times) + 1),
            times,
            marker='o',
            label=f"{src} → {dst}"
        )

    ax.set_title("Graphique de la répartition des temps de voyage unitaire par conversation")
    ax.set_xlabel("Nombre de paquets")
    ax.set_ylabel("Temps de voyage unitaire (secondes)")
    ax.legend(loc="best", fontsize="small")
    ax.grid(True)
    plt.tight_layout()
    plt.show()

    return None