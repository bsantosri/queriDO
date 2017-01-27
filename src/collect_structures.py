import getMateria
import getHtm

# Test script. This should get all docs from edition 1772.
ediParam = 3335
materias = getHtm.getedition(ediParam)
for materia in materias:
    matParam = materia['matId']
    tokens = getMateria.extract_tokens(materia)
    print('Outputting tokens to ../tokens/' + str(ediParam) + '-' + str(matParam) + '.txt')
    f = open('../tokens/' + str(ediParam) + '-' + str(matParam) + '.txt', 'wb')
    for item in tokens:
        f.write(item.encode('utf-8') + '\r\n')
    f.close()
