import webel

mol = webel.readstring("name", "chlorobenzene")
print(mol.write("smi"))

mol = webel.readstring("name", "aspirin")
print(mol.write("iupac"))

mol = webel.readstring("smi", "C1CN1")
mol.draw()
