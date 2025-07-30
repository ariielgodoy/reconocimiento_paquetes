# 🚀 Detección de Cajas y Bolsas con YOLO y Transfer Learning 🚀

En este proyecto, he utilizado **transfer learning** para entrenar un modelo **YOLO**, adaptándolo para detectar cajas y bolsas de manera más efectiva ya que ví que el tipo de cajas que se encontraban en las imagenes, no se detectaban bien con estos modelos.

---

## 💡 Mi Enfoque en el Entrenamiento

Para el entrenamiento del modelo, me basé en dos de las tres imágenes que me fueron proporcionadas. Dado el escaso número de ejemplos, decidí **ampliar el dataset** creando fondos artificiales, realizando rotaciones y perturbando las imágenes. El objetivo fue hacer el modelo más **robusto** y capaz de enfrentar diferentes situaciones.
Por otro lado, debido a que tengo una GTX 1050TI, he reducido el tamaño de las imagenes a 640x640 debido a que si lo dejaba como se nos fueron proporcionadas las imágenes, a lo mejor mi gráfica explota.

---

## 👀 Evaluación del Modelo

Utilicé la última imagen como una forma de evaluar el modelo, sin embargo, si lo quieren probar ustedes mismos, dejo un código en el repositorio el cual se llama probando_modelo.py. Aquí te muestro el resultado:

Como pueden ver, se detectan **casi todas las cajas y bolsas**.

<img width="970" height="972" alt="image" src="https://github.com/user-attachments/assets/d08e9896-34a0-4e71-be2d-0955de32cb2f" />



---

## 🎯 Ideas para Mejorar

Una mejora posible sería detectar la **cara superior de la caja o bolsa**. Con algo de **álgebra lineal**, se podría calcular la **normal del plano** que forma esa cara, lo que indicaría la dirección más favorable para realizar el "pick".

---

## 🌱 Mi Trayectoria y Proyecciones Futuras

Sé que mi solución actual no abarca completamente el problema ya que no he tenido la oportunidad de avanzar por mi cuenta tan rápido debido a que estoy realizando mis prácticas actualmente. Por otro lado, aún no he terminado la carrera; estoy a punto de empezar mi último año, donde veré temas de **sistemas de percepción** y para añadir, este año tengo asignado el TFG de la detección de conos con una cámara stereo para la competición de Formula Student AI, en donde la temática es la conducción autónoma. Además, en octubre, realizaré un curso de **deep learning** ofertado por el **Deep Learning Institute de Nvidia** para mejorar mis conocimientos, ya que todo lo que he mostrado aquí proviene de un curso de **machine learning** que hice el año pasado.

Al ver los problemas que se presentaban, me di cuenta de todo lo que me queda por aprender. Por ello, me gustaría que me tuvieran en cuenta para **futuras posiciones o incluso para prácticas**. A pesar de ser de Málaga, estoy dispuesto a **moverme a Barcelona** una vez que acabe la carrera para la realización de las mismas.

---

## Por último

De todas maneras, ¿sería posible conocer las soluciones de los participantes? A pesar de no poder aportar demasiado en las soluciones, me gustaría aprender del resto de la gente. O incluso si ustedes tienen la respuesta a los problemas.

¡Muchas gracias!
