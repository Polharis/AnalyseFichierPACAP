<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Mon Dashboard</title>
  <link rel="stylesheet" type="text/css" href="../static/style.css">
  <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
  <script src="../static/script.js"></script>
</head>
<body>
  <h1>Dashboard Analyse Réseau</h1>

  
  <button name="bouton_options" id="bouton_options" onclick="changer_etat_formulaire()">Ouvrir les options</button>
  <button onclick="generer()">Générer le graphique</button>


  <!-- Formulaire caché par défaut -->
  <div id="casePourFiltre">
    <h2>Options d'analyse</h2>
    

        <form id="formulaireFiltre" method = "GET">

            <label>IP uniquement</label>
            <input type="radio" id="proto_filtre" name="proto_filtre" value="ip_only"><br>

            <label>ARP uniquement</label> 
            <input type="radio" id="proto_filtre" name="proto_filtre" value="arp_only"><br>

            <label> Aucun filtre</label> 
            <input type="radio" name="proto_filtre" value="none" checked> <br>

            <input type="text" id = "ip_specifique" name = "ip_specifique" placeholder="IP spécifique à analyser"> <br>

            <input type="text" id = "protocol_specifique" name = "protocol_specifique" placeholder="Protocole à analyser"> <br>

            <input type="text" id = "port_specifique" name = "port_specifique" placeholder="Port à analyser"> <br>

            <input type="text" id = "plage_temps" name = "plage_temps" placeholder="Plage de temps en secondes"> <br>
            
        </form>
 </div>
 <!--   fin du formulaire-->
      

  <p id="chargement">Génération en cours...</p>
  <p id="erreur"></p>

  <div id="graphique" style="width:100%; height:600px;"></div>

  
</body>
</html>