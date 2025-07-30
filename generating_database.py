import cv2
import os
import random
import albumentations as A
import numpy as np
from rembg import remove


input_folder = "/home/ariel/github_repos/reconocimiento_paquetes/imagenes_redimensionadas"
label_folder = "/home/ariel/github_repos/reconocimiento_paquetes/imagenes_redimensionadas"
output_image_folder = "/home/ariel/github_repos/reconocimiento_paquetes/imagenes_aumentadas"
output_label_folder = "/home/ariel/github_repos/reconocimiento_paquetes/labels_aumentadas"
background_folder = "/home/ariel/github_repos/reconocimiento_paquetes/fondos"

os.makedirs(output_image_folder, exist_ok=True)
os.makedirs(output_label_folder, exist_ok=True)


transformations = [
    A.RandomRotate90(p=1.0),
    A.HorizontalFlip(p=1.0),
    A.RandomBrightnessContrast(p=1.0),
    A.ShiftScaleRotate(shift_limit=0.1, scale_limit=0.4, rotate_limit=30, p=1.0, border_mode=0),
    A.GaussNoise(p=1.0),
    A.RandomGamma(p=1.0),
    A.Blur(blur_limit=3, p=1.0),
    A.CLAHE(p=1.0),
]

num_augmentations = 50
backgrounds = [cv2.imread(os.path.join(background_folder, f)) for f in os.listdir(background_folder) if f.endswith(('.jpg', '.png'))]

def composite_with_random_background(foreground, alpha):
    bg = random.choice(backgrounds)
    bg = cv2.resize(bg, (foreground.shape[1], foreground.shape[0]))
    alpha = alpha.astype(float) / 255
    result = (foreground * alpha[..., None] + bg * (1 - alpha[..., None])).astype(np.uint8)
    return result

def load_yolo_labels(label_path, width, height):
    bboxes = []
    class_labels = []
    with open(label_path, 'r') as f:
        for line in f:
            cls, x, y, w, h = map(float, line.strip().split())
            x_min = (x - w / 2) * width
            y_min = (y - h / 2) * height
            x_max = (x + w / 2) * width
            y_max = (y + h / 2) * height
            bboxes.append([x_min, y_min, x_max, y_max])
            class_labels.append(int(cls))
    return bboxes, class_labels

def save_yolo_labels(path, bboxes, class_labels, img_w, img_h):
    with open(path, 'w') as f:
        for bbox, cls in zip(bboxes, class_labels):
            x_min, y_min, x_max, y_max = bbox
            x_center = (x_min + x_max) / 2 / img_w
            y_center = (y_min + y_max) / 2 / img_h
            w = (x_max - x_min) / img_w
            h = (y_max - y_min) / img_h
            f.write(f"{cls} {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f}\n")


for filename in os.listdir(input_folder):
    if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        continue

    image_path = os.path.join(input_folder, filename)
    label_path = os.path.join(label_folder, os.path.splitext(filename)[0] + '.txt')
    image = cv2.imread(image_path)

    if image is None or not os.path.exists(label_path):
        continue

    h, w = image.shape[:2]


    rgba = remove(image, alpha=True)
    alpha = rgba[:, :, 3]
    fg = rgba[:, :, :3]


    bboxes, class_labels = load_yolo_labels(label_path, w, h)

    for i in range(num_augmentations):
        composite = composite_with_random_background(fg, alpha)


        selected_transforms = random.sample(transformations, random.randint(1, 4))
        transform = A.Compose(
            selected_transforms,
            bbox_params=A.BboxParams(format='pascal_voc', label_fields=['class_labels'])
        )
        transformed = transform(image=composite, bboxes=bboxes, class_labels=class_labels)
        aug_image = transformed['image']
        aug_bboxes = transformed['bboxes']
        aug_labels = transformed['class_labels']


        out_name = f"{os.path.splitext(filename)[0]}_aug_bg{i}.jpg"
        out_img_path = os.path.join(output_image_folder, out_name)
        out_lbl_path = os.path.join(output_label_folder, os.path.splitext(out_name)[0] + '.txt')

        cv2.imwrite(out_img_path, aug_image)
        save_yolo_labels(out_lbl_path, aug_bboxes, aug_labels, aug_image.shape[1], aug_image.shape[0])

print("Imágenes aumentadas con cambio de fondo y etiquetas guardadas.")
