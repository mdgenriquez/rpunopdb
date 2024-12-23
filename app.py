import streamlit as st
import pandas as pd
import py3Dmol

# Configuración de la página de Streamlit
st.title("Visualización de Moléculas en 3D")
st.write("Sube un archivo CSV que contenga estructuras químicas en formato SMILES.")

# Cargar archivo CSV
uploaded_file = st.file_uploader("Sube tu archivo CSV", type="csv")

if uploaded_file:
    # Leer archivo CSV
    df = pd.read_csv(uploaded_file)
    st.write("Contenido del archivo:")
    st.write(df)

    # Verificar si existe una columna de SMILES
    if "SMILES" in df.columns:
        smiles_list = df["SMILES"].tolist()
        
        # Seleccionar una molécula para visualizar
        selected_smiles = st.selectbox("Selecciona un SMILES para visualizar:", smiles_list)
        
        # Renderizar la molécula en 3D
        if selected_smiles:
            viewer = py3Dmol.view(width=800, height=400)
            viewer.addModel(selected_smiles, "smi")  # Agregar SMILES
            viewer.setStyle({"stick": {}})    

