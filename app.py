import streamlit as st
import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

# Carga el archivo CSV
uploaded_file = st.file_uploader("Sube tu archivo CSV con SMILES", type="csv")
if uploaded_file:
    data = pd.read_csv(uploaded_file)

    # Verifica si existe una columna con SMILES
    if "SMILES" in data.columns:
        st.write("Archivo cargado correctamente.")
        smiles_list = data["SMILES"].tolist()

        # Selecciona una molécula para visualizar
        selected_smiles = st.selectbox("Selecciona una molécula para visualizar", smiles_list)

        # Genera la estructura 3D
        mol = Chem.MolFromSmiles(selected_smiles)
        mol = Chem.AddHs(mol)
        AllChem.EmbedMolecule(mol)
        AllChem.UFFOptimizeMolecule(mol)

        # Convierte la molécula a 3D
        mol_block = Chem.MolToMolBlock(mol)
        viewer = py3Dmol.view(width=800, height=400)
        viewer.addModel(mol_block, "mol")
        viewer.setStyle({"stick": {}})
        viewer.zoomTo()

        # Renderiza el visor 3D
        viewer.show()
    else:
        st.error("El archivo no contiene una columna 'SMILES'.")
