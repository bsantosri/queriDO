import getMateria
import getHtm

# Test script. This should get all docs from edition 1772.
ediParam = 1772
materias = getHtm.getedition(ediParam)
for materia in materias:
    matParam = materia['matId']
    htmlfile = getMateria.extract_html(materia)
    print('Outputting html to', '../html/' + str(ediParam) + '-' + str(matParam) + '.html')
    f = open('../html/' + str(ediParam) + '-' + str(matParam) + '.html', 'w')
    for line in htmlfile:
        f.write(line.encode('utf-8'))
    f.close()
