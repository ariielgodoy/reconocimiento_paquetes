import cv2
import numpy as np
import os
import random

output_folder = "/home/ariel/github_repos/reconocimiento_paquetes/fondos"
os.makedirs(output_folder, exist_ok=True)

num_fondos = 30

def generar_fondo_artificial(width=640, height=480):
    tipo = random.choice(['color', 'gradiente', 'ruido', 'rayas'])

    if tipo == 'color':
        color = tuple(random.randint(0, 255) for _ in range(3))
        fondo = np.full((height, width, 3), color, dtype=np.uint8)

    elif tipo == 'gradiente':
        x = np.linspace(0, 255, width).astype(np.uint8)
        gradient = np.tile(x, (height, 1))
        fondo = cv2.merge([gradient, gradient[::-1], np.full_like(gradient, random.randint(100, 200))])

    elif tipo == 'ruido':
        fondo = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

    elif tipo == 'rayas':
        fondo = np.zeros((height, width, 3), dtype=np.uint8)
        for i in range(0, width, random.randint(20, 60)):
            color = tuple(random.randint(100, 255) for _ in range(3))
            fondo[:, i:i+random.randint(5, 15)] = color

    return fondo


for i in range(num_fondos):
    fondo = generar_fondo_artificial()
    cv2.imwrite(os.path.join(output_folder, f"fondo_{i:02d}.jpg"), fondo)

print(f"✅ Se generaron {num_fondos} fondos artificiales en la carpeta '{output_folder}'.")
