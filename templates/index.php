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

  <button onclick="changer_etat_formulaire()">Ouvrir les options</button>
  <button onclick="generer()">Générer le graphique</button>


  <!-- Formulaire caché par défaut -->
  <div id="casePourFiltre">
    <h2>Options d'analyse</h2>
    

        <form id="formulaireFiltre" method = "POST">
            <label for="ip_only">IP uniquement</label>
            <input type="checkbox" id="ip_only" name="ip_only"> <br>

            <label for="arp_only">ARP uniquement</label>
            <input type="checkbox" id="arp_only" name="arp_only"> <br>

            <input type="text" id = "ip spécifique" name = "ip spécifique" placeholder="IP spécifique à analyser"> <br>

            <input type="text" id = "port" name = "port" placeholder="Port à analyser"> <br>

            <input type="text" id = "protocole" name = "protocole" placeholder="Protocole à analyser"> <br>
            
            <input type="submit" value="Valider" >
        </form>
 </div>
 <!--   fin du formulaire-->
      

  <p id="chargement">Génération en cours...</p>
  <p id="erreur"></p>

  <div id="graphique" style="width:100%; height:600px;"></div>

  
</body>
</html>