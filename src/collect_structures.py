import getMateria
import getHtm

# Test script. This should get all docs from edition 1772.
ediParam = 1772
materias = getHtm.getedition(ediParam)
for materia in materias:
    matParam = materia['matId']
    tokens = getMateria.extract_tokens(materia['matEdi'], materia['matId'])
    print('Outputting tokens to', '../tokens/' + str(ediParam) + '-' + str(matParam) + '.html')
    f = open('../tokens/' + str(ediParam) + '-' + str(matParam) + '.txt', 'w')
    for item in tokens:
        f.write(item.encode('utf-8') + '\n')
    f.close()
