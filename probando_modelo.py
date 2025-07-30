import cv2
from ultralytics import YOLO

model_path = '/home/ariel/runs/detect/train2/weights/best.pt'
model = YOLO(model_path)
conf_threshold = 0.7

image_path = '/home/ariel/github_repos/reconocimiento_paquetes/imagenes_redimensionadas/IMG_9104_640.jpg'
img = cv2.imread(image_path)
if img is None:
    print(f"Error: no se pudo cargar la imagen {image_path}")
    exit()

results = model(img)[0]

boxes = []
confidences = []
class_ids = []

for box in results.boxes:
    conf = box.conf.item()
    if conf >= conf_threshold:
        boxes.append(box.xyxy[0].cpu().numpy())
        confidences.append(conf)
        class_ids.append(int(box.cls.cpu().item()))

for box, conf, cls_id in zip(boxes, confidences, class_ids):
    x1, y1, x2, y2 = map(int, box)
    label = f"{model.names[cls_id]} {conf:.2f}"
    color = (0, 255, 0)
    cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
    cv2.putText(img, label, (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

# Escalar imagen para mostrarla más grande, ejemplo 3x
scale_percent = 300  # porcentaje de escala
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
img_resized = cv2.resize(img, dim, interpolation=cv2.INTER_LINEAR)

# Crear ventana redimensionable y mostrar imagen
cv2.namedWindow('Detección YOLO', cv2.WINDOW_NORMAL)
cv2.imshow('Detección YOLO', img_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
