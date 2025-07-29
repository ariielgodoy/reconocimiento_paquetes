import cv2
import os
import random
import albumentations as A
import numpy as np

# Carpetas
input_folder = "C:/Users/emc/Desktop/ariel/challenge/Coding-challenge/coding-challenge/3_normal_picking_angle"
output_folder = "C:/Users/emc/Desktop/ariel/challenge/imagenes_aumentadas"
os.makedirs(output_folder, exist_ok=True)

# Lista de transformaciones que se aplicarán aleatoriamente
transformations = [
    A.RandomRotate90(p=1.0),
    A.Flip(p=1.0),
    A.RandomBrightnessContrast(p=1.0),
    A.ShiftScaleRotate(shift_limit=0.1, scale_limit=0.5, rotate_limit=45, p=1.0),
    A.GaussNoise(p=1.0),
    A.RandomGamma(p=1.0),
    A.Blur(blur_limit=3, p=1.0),
    A.CLAHE(p=1.0),
]

num_augmentations = 50

def read_label(txt_path):
    """Lee un archivo de etiquetas y devuelve las coordenadas y clases."""
    boxes = []
    with open(txt_path, 'r') as f:
        for line in f.readlines():
            class_id, x_center, y_center, width, height = map(float, line.strip().split())
            boxes.append([class_id, x_center, y_center, width, height])
    return boxes

def write_label(txt_path, boxes):
    """Escribe las coordenadas transformadas de las cajas en un archivo .txt."""
    with open(txt_path, 'w') as f:
        for box in boxes:
            f.write(f"{int(box[0])} {box[1]} {box[2]} {box[3]} {box[4]}\n")

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(input_folder, filename)
        label_path = os.path.splitext(image_path)[0] + '.txt'

        if not os.path.exists(label_path):
            continue  # Si no existe el archivo de etiquetas, lo saltamos

        # Cargar imagen y etiquetas
        image = cv2.imread(image_path)
        boxes = read_label(label_path)

        if image is None or len(boxes) == 0:
            continue

        # Aumentación de imágenes
        for i in range(num_augmentations):
            selected_transforms = random.sample(transformations, random.randint(1, 4))
            transform = A.Compose(selected_transforms)

            # Aplicamos la transformación a la imagen y las cajas
            augmented = transform(image=image)
            aug_image = augmented['image']

            # También necesitamos aplicar las transformaciones a las cajas
            augmented_boxes = []
            for box in boxes:
                class_id, x_center, y_center, width, height = box

                # Convertir las coordenadas a valores entre 0 y 1
                h, w, _ = image.shape
                x_center /= w
                y_center /= h
                width /= w
                height /= h

                # Crear un diccionario con las coordenadas de la caja
                augmented_boxes.append([class_id, x_center, y_center, width, height])

            # Guardar imagen aumentada
            aug_image_filename = f"{os.path.splitext(filename)[0]}_aug_{i}.jpg"
            aug_image_path = os.path.join(output_folder, aug_image_filename)
            cv2.imwrite(aug_image_path, aug_image)

            # Guardar archivo de etiquetas correspondiente
            aug_label_filename = os.path.splitext(aug_image_filename)[0] + '.txt'
            aug_label_path = os.path.join(output_folder, aug_label_filename)
            write_label(aug_label_path, augmented_boxes)

print(f"Generadas {num_augmentations * len(os.listdir(input_folder))} imágenes y etiquetas aumentadas.")
