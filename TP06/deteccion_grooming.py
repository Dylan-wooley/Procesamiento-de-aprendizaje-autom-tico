import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

df = pd.DataFrame({
    'mensaje': [
        "¿Cuántos años tenés? No le digas a nadie que hablamos.",
        "Hola, ¿cómo estás? ¿Querés jugar algo online?",
        "Sos muy linda, no le muestres esto a tus papás.",
        "¿Terminaste la tarea de matemáticas?",
        "Podés mandarme una foto tuya, pero que sea solo para mí.",
        "¿Querés que te ayude con el juego que no podías pasar?",
        "No le contés a nadie que hablamos por acá, ¿sí?",
        "¿Te gustó la película de ayer?",
        "¿Estás solo en casa ahora?",
        "¿Querés hacer una videollamada para estudiar juntos?",
        "No le digas a tus padres que te escribí, es nuestro secreto.",
        "¿Cómo te fue en el examen de historia?",
        "Mandame una foto tuya, pero que nadie más la vea.",
        "¿Jugamos Minecraft esta tarde?",
        "Sos muy especial para mí, no le cuentes a nadie lo que hablamos.",
        "¿Querés que te pase los apuntes de biología?",
        "¿Podés mostrarme cómo estás vestida ahora?",
        "¿Tenés ganas de salir a andar en bici mañana?",
        "No hace falta que le digas a nadie que hablamos tanto.",
        "¿Querés que estudiemos juntos para el parcial?"
    ],
    'etiqueta': [
        'grooming', 'no grooming', 'grooming', 'no grooming', 'grooming',
        'no grooming', 'grooming', 'no grooming', 'grooming', 'no grooming',
        'grooming', 'no grooming', 'grooming', 'no grooming', 'grooming',
        'no grooming', 'grooming', 'no grooming', 'grooming', 'no grooming'
    ]
})

#  recordatorio (70% entrenamiento, 30% prueba)
vectorizador = CountVectorizer()
X = vectorizador.fit_transform(df['mensaje'])
y = df['etiqueta']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

modelo = MultinomialNB()
modelo.fit(X_train, y_train)

predicciones_prueba = modelo.predict(X_test)

print("--- INFORME DEL MODELO ---")
print(f"1. Precisión total (accuracy): {accuracy_score(y_test, predicciones_prueba)}")
print("\n2. Reporte de clasificación:")
print(classification_report(y_test, predicciones_prueba))
print("3. Matriz de confusión (grooming, no grooming):")
print(confusion_matrix(y_test, predicciones_prueba, labels=['grooming', 'no grooming']))

nuevos_mensajes = [
    "¿Podés mandarme una foto tuya? No se la muestres a nadie.",
    "¿Jugamos Minecraft esta tarde?",
    "No le digas a tus papás que hablamos, ¿sí?",
    "¿Terminaste el trabajo práctico de historia?"
]

nuevas_X = vectorizador.transform(nuevos_mensajes)
predicciones_nuevas = modelo.predict(nuevas_X)

print("\n4. Clasificación de nuevos mensajes:")
for mensaje, resultado in zip(nuevos_mensajes, predicciones_nuevas):
    print(f'"{mensaje}" → {resultado}')