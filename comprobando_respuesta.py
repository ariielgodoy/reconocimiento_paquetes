import cv2

# Función para leer el archivo .txt y obtener las coordenadas
def read_annotations(txt_file):
    boxes = []
    with open(txt_file, 'r') as f:
        for line in f.readlines():
            parts = line.strip().split()
            class_id = int(parts[0])  # Clase (0 para cajas, 2 para flechas, etc.)
            x_center = float(parts[1])
            y_center = float(parts[2])
            w = float(parts[3])
            h = float(parts[4])
            boxes.append((class_id, x_center, y_center, w, h))
    return boxes

# Función para dibujar la caja
def draw_box(image, x_center, y_center, w, h, color=(0, 255, 0), thickness=2):
    x_min = int((x_center - w / 2) * image.shape[1])
    y_min = int((y_center - h / 2) * image.shape[0])
    x_max = int((x_center + w / 2) * image.shape[1])
    y_max = int((y_center + h / 2) * image.shape[0])
    cv2.rectangle(image, (x_min, y_min), (x_max, y_max), color, thickness)
    return image

# Función para dibujar la flecha (si la clase es 2)
def draw_arrow(image, x_center, y_center, w, h, color=(0, 0, 255), thickness=2):
    start_point = (int(x_center * image.shape[1]), int(y_center * image.shape[0]))
    end_point = (int(x_center * image.shape[1]), int((y_center + 0.1) * image.shape[0]))  # Apuntando hacia abajo
    cv2.arrowedLine(image, start_point, end_point, color, thickness)
    return image

# Carpeta de entrada (imágenes)
input_image_path = r"C:\Users\emc\Desktop\ariel\challenge\imagenes_redimensionadas\IMG_9104_640.jpg"
txt_file_path = r"C:\Users\emc\Desktop\ariel\challenge\imagenes_redimensionadas\IMG_9104_640.txt"

# Cargar imagen
image = cv2.imread(input_image_path)

# Leer las coordenadas de las cajas desde el archivo .txt
boxes = read_annotations(txt_file_path)

# Dibujar cajas y flechas
for box in boxes:
    class_id, x_center, y_center, w, h = box

    # Si es una caja, dibujarla
    if class_id == 0 or 1:
        image = draw_box(image, x_center, y_center, w, h)
    
    # Si es una flecha (class_id == 2), dibujar la flecha
    elif class_id == 2:
        image = draw_arrow(image, x_center, y_center, w, h)

# Mostrar la imagen con las cajas y las flechas
cv2.imshow("Image with Boxes and Arrows", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Guardar la imagen resultante (opcional)
cv2.imwrite("output_image.jpg", image)
