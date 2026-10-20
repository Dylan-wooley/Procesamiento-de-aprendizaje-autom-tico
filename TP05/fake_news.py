import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split

df = pd.DataFrame({
    'texto': [
        "El presidente anunció una nueva reforma educativa",
        "Descubren que la vacuna convierte a las personas en robots",
        "La NASA confirma el hallazgo de agua en Marte",
        "Científicos afirman que la Tierra es plana",
        "El ministerio de salud lanza campaña contra el dengue",
        "Celebridades usan crema milagrosa para rejuvenecer 30 años",
        "Se inaugura el nuevo hospital en la ciudad",
        "Estudio revela que comer chocolate cura el cáncer",
        "Gobierno aprueba ley de protección ambiental",
        "Investigadores aseguran que los teléfonos espían nuestros sueños"
    ],
    'etiqueta': ['real', 'fake', 'real', 'fake', 'real', 'fake', 'real', 'fake', 'real', 'fake']
})

vectorizador = CountVectorizer()
X = vectorizador.fit_transform(df['texto'])
y = df['etiqueta']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

modelo = MultinomialNB()
modelo.fit(X_train, y_train)

predicciones_prueba = modelo.predict(X_test)
print(f"Precisión total (accuracy): {accuracy_score(y_test, predicciones_prueba)}")
print("Matriz de confusión (fake, real):")
print(confusion_matrix(y_test, predicciones_prueba, labels=['fake', 'real']))

nuevas_noticias = [
    "Nuevo estudio demuestra que el café mejora la memoria",
    "Expertos afirman que los gatos pueden hablar con humanos"
]

nuevas_X = vectorizador.transform(nuevas_noticias)
predicciones_nuevas = modelo.predict(nuevas_X)

print("\nClasificación de nuevas noticias:")
for noticia, resultado in zip(nuevas_noticias, predicciones_nuevas):
    print(f'"{noticia}" → {resultado}')