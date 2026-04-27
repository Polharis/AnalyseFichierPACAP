import matplotlib.pyplot as plt
import pandas as pd
import base64
import io

#pour plotly
import plotly.graph_objects as go
import plotly.express as px
import json


def statistiqueSousgraphique(stats_table, graph_type) : 
    #Cette fonction prend en entrée une table de statistiques et retourne un graphique 
    # Réaliser avec plotly pour retourner du JSON
    stats_table.pop("total_paquet", None)
    liste_cle_a_supprimer = []
    for key in stats_table.keys() :
        if stats_table[key] < 0.5 :
            liste_cle_a_supprimer.append(key)
    for key in liste_cle_a_supprimer :
        stats_table.setdefault("Other", 0)
        stats_table["Other"] += stats_table[key]
        stats_table.pop(key, None)

    # Déterminer le type d'information
    if graph_type == "CoucheServiceDestination" or graph_type == "CoucheServiceSource" :
        information = "services"
    else : 
        information = "protocoles"

    # Créer le graphique en camembert avec Plotly
    fig = go.Figure(data=[go.Pie(
        labels=list(stats_table.keys()),
        values=list(stats_table.values()),
        textposition='inside',
        textinfo='percent+label'
    )])

    fig.update_layout(
        title=f"Graphique des statistiques de la {graph_type}",
        xaxis_title=f"Pourcentage de {information} sur l'ensemble des paquets"
    )

    return fig.to_json()


#Créer un histogramme de l'inter-espacement entre les paquets pour chaque conversation (src, dst)
def histogrammeIntraEspacement(dicoReseau,plage_temps_graphique) :
    fig = go.Figure()

    for (src, dst), times in dicoReseau.items():
        if not times:
            continue
        fig.add_trace(go.Histogram(
            x=times,
            name=f"{src} → {dst}",
            opacity=0.6,
            xbins=dict(size=plage_temps_graphique)  
        ))

    fig.update_layout(
        title="Histogramme des inter-espacements par conversation",
        xaxis_title="Inter-espacement (millisecondes)",
        yaxis_title="Nombre d'intervalles",
        barmode='overlay'
    )

    return fig.to_json()

def courbeRepartitionIntraEspacement(dicoReseau,plage_temps_graphique) :
    fig = go.Figure()

    liste_temps = []
    dico_temps_pourcent = {}
    for valeures in dicoReseau.values():
        for temps in valeures : 
            liste_temps.append(temps)
    liste_temps.sort()
    
    # Regrouper les temps par plage_temps_graphique et compter les occurrences
    for temps in liste_temps :
        temps_arrondi = round(temps / plage_temps_graphique) * plage_temps_graphique
        dico_temps_pourcent.setdefault(temps_arrondi, 0)
        dico_temps_pourcent[temps_arrondi] += 1
    
    # Calculer les pourcentages
    total = len(liste_temps)
    for temps_arrondi in dico_temps_pourcent :
        dico_temps_pourcent[temps_arrondi] = (dico_temps_pourcent[temps_arrondi] / total) * 100
    
    # Trier le dictionnaire par temps
    temps_tries = sorted(dico_temps_pourcent.keys())
    pourcentages = [dico_temps_pourcent[t] for t in temps_tries]
    
    # Calculer les pourcentages cumulatifs
    cumulative = []
    cumul = 0
    for pourcent in pourcentages :
        cumul += pourcent
        cumulative.append(cumul)
    
    # Ajouter la courbe de répartition cumulative
    fig.add_trace(go.Scatter(
        x=temps_tries,
        y=cumulative,
        mode='lines+markers',
        name='Répartition cumulative',
        line=dict(color='blue', width=2)
    ))
    
    fig.update_layout(
        title="Courbe de répartition cumulative des inter-espacements",
        xaxis_title="Inter-espacement (millisecondes)",
        yaxis_title="Pourcentage cumulatif (%)",
        hovermode='x unified'
    )

    return fig.to_json()


def choisirGraphique(stats_table, typeGraphique) :
    if typeGraphique == "CoucheDeux" or typeGraphique == "CoucheTrois" or typeGraphique == "CoucheServiceSource" or typeGraphique == "CoucheServiceDestination" :
        return statistiqueSousgraphique(stats_table, typeGraphique)
    elif typeGraphique == "InterEspacement" :
        return histogrammeIntraEspacement(stats_table)
    else : 
        return None










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