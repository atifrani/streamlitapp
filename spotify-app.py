import streamlit as st
import pandas as pd
import duckdb

# fonction pour charger les données spotify depuis un fichier CSV sur kaggle
def charger_donnees_spotify():
    url = "https://www.kaggle.com/datasets/zaheenhamidani/ultimate-spotify-tracks-db/download?datasetVersionNumber=1"
    return pd.read_csv(url) 

# Initialiser la connexion DuckDB
conn = duckdb.connect(database=':memory:', read_only=False)

# Sidebar pour le chargement des données
st.sidebar.title("Source de données")
source_option = st.sidebar.radio(
    "Choisir la source de données:",
    ["Données Spotify de démonstration", "Télécharger un fichier CSV"]
)

# Obtenir les données
if source_option == "Données Spotify de démonstration":
    df = charger_donnees_spotify()
    st.sidebar.success("Données Spotify de démonstration chargées!")
    
    # Enregistrer les données dans DuckDB
    conn.execute("CREATE TABLE IF NOT EXISTS spotify AS SELECT * FROM df")
    
else:
    uploaded_file = st.sidebar.file_uploader("Télécharger un fichier CSV", type=["csv"])
    if uploaded_file is not None:
        # Sauvegarder temporairement le fichier
        with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_path = tmp_file.name
        
        # Créer une table à partir du CSV avec DuckDB
        conn.execute(f"CREATE TABLE IF NOT EXISTS spotify AS SELECT * FROM read_csv_auto('{tmp_path}')")
        
        # Charger les données pour affichage
        df = conn.execute("SELECT * FROM spotify").fetchdf()
        st.sidebar.success(f"{len(df)} morceaux chargés!")
        
        # Supprimer le fichier temporaire
        os.unlink(tmp_path)
    else:
        st.info("Veuillez télécharger un fichier CSV ou utiliser les données de démonstration.")
        st.stop()
