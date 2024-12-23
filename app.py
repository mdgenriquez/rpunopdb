import py3Dmol

# Visualiza una molécula en formato SMILES
smiles = "C1=CC=CC=C1"  # Un SMILES de ejemplo
viewer = py3Dmol.view(width=800, height=400)
viewer.addModel(smiles, "smi")  # Usar SMILES directamente
viewer.setStyle({"stick": {}})
viewer.zoomTo()
viewer.show()
