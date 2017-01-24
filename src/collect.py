import getMateria
import getHtm

# Test script. This should get all docs from edition 1772.
materias = getHtm.getedition(1772)
for materia in materias:
    getMateria.extract_html(materia['matEdi'], materia['matId'])
