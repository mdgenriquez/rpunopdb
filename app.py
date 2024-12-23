import py3Dmol

# Visualiza una molécula en SMILES
smiles = "C1=CC=CC=C1"  # Ejemplo de SMILES
viewer = py3Dmol.view(width=800, height=400)
viewer.addModel(smiles, "smi")
viewer.setStyle({"stick": {}})
viewer.zoomTo()

# Renderiza en Streamlit
import streamlit as st
st.write(viewer.show())
