    est_formulaire_filtre_ouvert = false;
    function changer_etat_formulaire(){
        if (est_formulaire_filtre_ouvert) {
            fermerFormulaire();
            est_formulaire_filtre_ouvert = false;
        } else {
            afficherFormulaire();
            est_formulaire_filtre_ouvert = true;
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


    async function generer() {
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
        

      const filtres = {
        proto_filtre: proto_filtre,
        ip_specifique: ip_specifique,
        protocol_specifique: protocol_specifique,
        port_specifique: port_specifique,
        plage_temps: plage_temps
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