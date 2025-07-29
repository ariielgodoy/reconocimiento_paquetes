from ultralytics import YOLO
import cv2

# Carga el modelo YOLOv8 preentrenado
model = YOLO("yolov8n.pt")

# Carga la imagen donde quieres detectar maletas
image = cv2.imread("maletas.jpg")  # Cambia por tu archivo

# Ejecuta la detección con un umbral de confianza (ejemplo 0.3)
results = model(image, conf=0.15)

# Clase para maletas
maleta_class_id = 28

# Recorre todas las detecciones y dibuja solo maletas
for box in results[0].boxes:
    class_id = int(box.cls[0])
    if class_id == maleta_class_id:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf[0])
        label = model.model.names[class_id]
        # Dibuja rectángulo verde
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        # Pone etiqueta con confianza
        cv2.putText(image, f"{label} {conf:.2f}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Muestra la imagen con maletas detectadas
cv2.imshow("Maletas detectadas", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
