
import getMateria
import getHtm

# Test script. This should get all docs from edition 1772.
ediParam = 3335
materias = getHtm.getedition(ediParam)
tokens = []
for materia in materias:
    matParam = materia['matId']
    tokens.append(str(getMateria.extract_tokens(materia)))

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(min_df=1)
tfidf = vectorizer.fit_transform(tokens)
print vectorizer.vocabulary_
