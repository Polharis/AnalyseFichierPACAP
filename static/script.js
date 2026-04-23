    est_formulaire_filtre_ouvert = false;
    est_options_graphique_ouvert = false;
    est_options_statistique_ouvert = false;

    function changer_etat_formulaire(){
        if (est_formulaire_filtre_ouvert) {
            fermerFormulaire();
            est_formulaire_filtre_ouvert = false;
        } else {
            cacherToutElement()
            afficherFormulaire();
            est_formulaire_filtre_ouvert = true;
        }
    }

    function changer_etat_option_graphique(){
        if (est_options_graphique_ouvert) {
            cacherOptionGraphique();
            est_options_graphique_ouvert = false;

        } else {
            cacherToutElement()
            afficherOptionGraphique();
            est_options_graphique_ouvert = true;
        }
    }

    function changer_etat_option_statistique(){
        
        if (est_options_statistique_ouvert) {
            cacherOptionStatistique();
            est_options_statistique_ouvert = false;
        } else {
            cacherToutElement()
            afficherOptionStatistique();
            est_options_statistique_ouvert = true;
        }
    }
    

    function afficherFormulaire() {
      document.getElementById('casePourFiltre').style.display = 'block';
      document.getElementById('bouton_options').textContent = 'Fermer les options';
    }

    function fermerFormulaire() {
      document.getElementById('casePourFiltre').style.display = 'none';
      document.getElementById('bouton_options').textContent = 'Ouvrir les options';
    }

    function afficherOptionGraphique() {
        document.getElementById('casePourGraphique').style.display = 'block';
        document.getElementById('buttonGraphics').textContent = 'Fermer les options graphiques';
    }

    function cacherOptionGraphique() {
        document.getElementById('casePourGraphique').style.display = 'none';
        document.getElementById('buttonGraphics').textContent = 'Ouvrir les options graphiques';
        document.getElementById('graphique').style.display = 'none';
    }

    function afficherOptionStatistique() {
        document.getElementById('casePourStatstique').style.display = 'block';
        document.getElementById('buttonStatistics').textContent = 'Fermer les options statistiques';
    }

    function cacherOptionStatistique() {
        document.getElementById('casePourStatstique').style.display = 'none';
        document.getElementById('buttonStatistics').textContent = 'Ouvrir les options statistiques';
        document.getElementById('statistique').style.display = 'none';
    }

    function cacherToutElement() {
      document.getElementById('casePourFiltre').style.display = 'none';
      document.getElementById('casePourGraphique').style.display = 'none';
      document.getElementById('casePourStatstique').style.display = 'none';
      document.getElementById('graphique').style.display = 'none';
      document.getElementById('statistique').style.display = 'none';
      document.getElementById('succesCSV').style.display = 'none';
      document.getElementById('erreur').textContent = '';
    }


    async function genererRapportCsv() {
      try {
        // Affiche le message de chargement
        document.getElementById('chargement').style.display = 'block';
        document.getElementById('erreur').textContent = '';

        // filtres sur les données 
        const proto_filtre = document.querySelector('input[name="proto_filtre"]:checked').value;
        const ip_specifique = document.getElementById('ip_specifique').value;
        const protocol_specifique = document.getElementById('protocol_specifique').value;
        const port_specifique = document.getElementById('port_specifique').value;
        const plage_temps = document.getElementById('plage_temps').value;
        const chemin_fichier = document.getElementById('fichier_pcap').value;

        const filtres = {
        proto_filtre: proto_filtre,
        ip_specifique: ip_specifique,
        protocol_specifique: protocol_specifique,
        port_specifique: port_specifique,
        plage_temps: plage_temps,
        chemin_fichier: chemin_fichier
        };
        

        const res = await fetch('/genererRapportCsv', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(filtres)
        });

        const data = await res.json();



        document.getElementById('chargement').style.display = 'none';
        if (data.success) {
          document.getElementById('succesCSV').style.display = 'block';
        } else {
          document.getElementById('erreur').textContent = 'Erreur : ' + data.error;
        }

       
        } catch (error) {
            console.error('Erreur:', error);
            document.getElementById('erreur').textContent = 'Erreur: ' + error.message;
            document.getElementById('chargement').style.display = 'none';
      }
    }



    async function generer(typeGraphique) {
      try {
        // Affiche le message de chargement
        document.getElementById('chargement').style.display = 'block';
        document.getElementById('graphique').style.display = 'none';
        document.getElementById('erreur').textContent = '';

        // filtres sur les données 
        const proto_filtre = document.querySelector('input[name="proto_filtre"]:checked').value;
        const ip_specifique = document.getElementById('ip_specifique').value;
        const protocol_specifique = document.getElementById('protocol_specifique').value;
        const port_specifique = document.getElementById('port_specifique').value;
        const plage_temps = document.getElementById('plage_temps').value;
        const chemin_fichier = document.getElementById('fichier_pcap').value;
        

      const filtres = {
        proto_filtre: proto_filtre,
        ip_specifique: ip_specifique,
        protocol_specifique: protocol_specifique,
        port_specifique: port_specifique,
        plage_temps: plage_temps,
        typeGraphique: typeGraphique,
        chemin_fichier: chemin_fichier
      };

     

      const res = await fetch('/generer', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(filtres)
      });
      

      const data = await res.json();



      document.getElementById('chargement').style.display = 'none';

      if (data.success) {
          const fig = JSON.parse(data.graphique);
          const div = document.getElementById('graphique');
          div.style.display = 'block';  // ← réaffiche le div
          Plotly.newPlot('graphique', fig.data, fig.layout);
      } else {
          document.getElementById('erreur').textContent = 'Erreur : ' + data.error;
      }
      } catch (error) {
        console.error('Erreur:', error);
        document.getElementById('erreur').textContent = 'Erreur: ' + error.message;
        document.getElementById('chargement').style.display = 'none';
      }
    }

    async function genererRapportStatistique(typeStatistique) {
      try {
        // Affiche le message de chargement
        document.getElementById('chargement').style.display = 'block';
        document.getElementById('erreur').textContent = '';

        // filtres sur les données 
        const proto_filtre = document.querySelector('input[name="proto_filtre"]:checked').value;
        const ip_specifique = document.getElementById('ip_specifique').value;
        const protocol_specifique = document.getElementById('protocol_specifique').value;
        const port_specifique = document.getElementById('port_specifique').value;
        const plage_temps = document.getElementById('plage_temps').value;
        const chemin_fichier = document.getElementById('fichier_pcap').value;

        const filtres = {
        proto_filtre: proto_filtre,
        ip_specifique: ip_specifique,
        protocol_specifique: protocol_specifique,
        port_specifique: port_specifique,
        plage_temps: plage_temps,
        chemin_fichier: chemin_fichier,
        typeStatistique: typeStatistique
        };
        

        const res = await fetch('/genererRapportStatistique', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(filtres)
        });

        const responseText = await res.text();
        const data = JSON.parse(responseText);

        document.getElementById('chargement').style.display = 'none';
        
        if (data.success) {
          document.getElementById('statistique').textContent = data.statistique;
          document.getElementById('statistique').style.display = 'block';
        } else {
            document.getElementById('erreur').textContent = 'Erreur : ' + data.error;
        }
        } catch (error) {
          console.error('Erreur:', error);
          document.getElementById('erreur').textContent = 'Erreur: ' + error.message;
          document.getElementById('chargement').style.display = 'none';
        }
    }