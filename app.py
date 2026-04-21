from flask import Flask, render_template, request, jsonify
import matplotlib
matplotlib.use('Agg')  # Important : mode sans affichage
import matplotlib.pyplot as plt
import io, base64
import subprocess

import scriptPy.graphiques.creationGraphiques as graphiques
import scriptPy.LectureDonne.optionsArgParse as options
import  scriptPy.LectureDonne.lectureDonneFichierUnique as recupDico  
import statistiques.creationRapportStats as stats



app = Flask(__name__)




def fig_to_base64(fig):
    """Convertit la figure en base64 sans toucher au disque"""
    buf = io.BytesIO()          # Un "fichier" en mémoire vive
    fig.savefig(buf, format='png', bbox_inches='tight', dpi=150)
    buf.seek(0)                 # Remet le curseur au début
    img_b64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)              # Libère la mémoire matplotlib
    return img_b64

@app.route('/')
def index():
    return render_template('index.html')  

@app.route('/generer', methods=['POST'])
def generer():
    params = request.get_json(force=True, silent=True) or {}
    dicoReseau = recupDico.get_table_par_protocole()
    fig = graphiques.histogrammeInterEspacement(stats.liste_différence_src_dst_adjacente(dicoReseau))

    if fig is None:
        return jsonify({ 'success': False, 'error': 'Aucune donnée disponible.' })

    return jsonify({ 'success': True, 'graphique': fig })  



    

   

app.run(debug=True, host='127.0.0.1', port=5000)

#liste chemin du fichier PCAP à analyser
#/home/stagetesa/Downloads/NMAP_PROBE.pcap

#liste filtre 
#CoucheDeux
#CoucheTrois
#CoucheServiceSource
#CoucheServiceDestination
#InterEspacement

#liste graphique
#CoucheDeux
#CoucheTrois
#CoucheServiceSource
#CoucheServiceDestination   