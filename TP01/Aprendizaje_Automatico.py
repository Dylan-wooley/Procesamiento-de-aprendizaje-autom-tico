def Clasificacion(Usuarios):
    for u in Usuarios:

        if "victoria" in u or "derrota" in u:
            print("Categoría: Combate")
        elif "descubrimiento" in u or "sin_hallazgos" in u:
            print("Categoría: Exploración")
        elif "mensaje_enviado" in u:
            print("Categoría: Interacción Social")


Usuarios = [
    ["user01", 120, "victoria"],
    ["user02", 300, "descubrimiento"],
    ["user03", 180, "mensaje_enviado"],
    ["user04", 90, "derrota"],
    ["user05", 240, "sin_hallazgos"],
]

Clasificacion(Usuarios)


'''
1. ¿Qué reglas funcionaron mejor para clasificar las acciones?

Las reglas que buscan palabras clave exactas en la columna de Resultado funcionaron perfecto para estos ejemplos: 

-Combate: Buscar si decía "victoria" o "derrota" sirvió para agrupar las peleas sin fallar.  

-Exploración: Buscar "descubrimiento" o "sin_hallazgos".   

-Interacción Social: Buscar "mensaje_enviado".   

Funcionaron bien porque en esta tabla chica cada palabra solo pertenecía a un solo tipo de actividad.   



2. ¿Qué limitaciones tiene este enfoque basado en reglas?

-Es poco práctico si el juego crece: Si mañana se agregan acciones nuevas (como "empatar", "escapar" o "vender")
 hay que meterse al código a escribir más if a mano uno por uno.

-No perdona errores: Si una palabra viene con mayúscula, un error de tipeo o un sinónimo (por ejemplo, "Victoria" o "triunfo")
 el programa no la reconoce y no hace nada.

-Ignora datos útiles: El código no usa para nada el tiempo en segundos, perdiendo pistas importantes
 como que las peleas suelen durar poco y explorar suele tomar más tiempo.   

 

3. ¿Cómo se podría mejorar la clasificación utilizando modelos de machine learning más avanzados?

-Aprender de muchas cosas a la vez: Una inteligencia artificial puede mirar al mismo tiempo los segundos jugados y el resultado
 sacando conclusiones más completas en lugar de fijarse en una sola palabra.   

-Entender situaciones nuevas: Si el sistema aprende de muchos ejemplos pasados, puede adivinar la categoría de una jugada nueva por sí solo,
 sin que tengamos que escribirle una regla fija para cada caso.
 
-Reconocer sinónimos: Puede darse cuenta de que palabras como "ganó", "victoria" y "triunfó" significan básicamente lo mismo.
'''