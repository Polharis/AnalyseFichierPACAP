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
    }

    function fermerFormulaire() {
      document.getElementById('casePourFiltre').style.display = 'none';
    }


    async function generer() {
      // Affiche le message de chargement
      document.getElementById('chargement').style.display = 'block';
      document.getElementById('graphique').style.display = 'none';
      document.getElementById('erreur').textContent = '';

      const res = await fetch('/generer', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({})
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
    }