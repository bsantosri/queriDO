import getMateria
import getHtm

# Test script. This should get all docs from edition 1772.
materias = getHtm.getedition(1772)
for materia in materias:
    dados = getMateria.extract(materia['matId'], materia['matEdi'])
    for text in dados:
        print(text.encode('utf-8'))
