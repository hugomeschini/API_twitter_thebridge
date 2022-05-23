# API_twitter_thebridge

1. Recopilar los tweets donde se mencione la cuenta de @TheBridge_Tech desde comienzo de año hasta el día de ayer incluído. Se recomienda utilizar la API de
Twitter. Se deberá recoger:
a. Id del mensaje
b. Cuerpo del texto del mensaje
c. Fecha del tweet
d. Id del autor
e. Nombre del autor
f. Nombre de usuario del autor
g. Métricas públicas del tweet (retweet, reply, like, quote)

2. Almacenarlos en una base de datos SQL en 2 tablas diferentes a tu elección.

3. Realizar un pequeño análisis donde se respondan a las siguientes preguntas de negocio:
a. ¿Cuál es el tweet con mayor repercusión social?
b. ¿Cuál es el usuario que más menciona a la escuela?
c. ¿En qué mes se concentra el mayor número de tweets?
d. ¿Qué palabras son más frecuentes?
e. ¿Qué tipo de correlación matemática encuentras entre las métricas públicas?

4. Utiliza un modelo pre entrenado (ds_thebridge_1_22\3-Machine_Learning\5-NLP\NLTK&CountVectorizer\data\output\finished_model.model) para determinar el sentimiento de los 3 tweets con mayor repercusión. Preguntas:
a. ¿Cuáles son las predicciones? Interpreta los resultados.
b. ¿Qué variables han podido influir más en las predicciones del modelo?
c. ¿Cómo podrías mejorar el modelo?
d. ¿Qué otras oportunidades se te ocurren donde se podrían aplicar otros modelos de ML?

5. Despliega el modelo (no en local, puedes elegir el proveedor), con un endpoint donde poder enviarle un cuerpo de texto y devuelva la predicción del sentimiento.

6. Realizar una presentación de 5 minutos máximo, donde presentes tu solución y la defiendas en una entrevista personal.
