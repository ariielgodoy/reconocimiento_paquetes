import cv2
import os

input_folder = "/home/ariel/github_repos/reconocimiento_paquetes/Coding-challenge/coding-challenge/3_normal_picking_angle"
output_folder = "/home/ariel/github_repos/reconocimiento_paquetes/imagenes_redimensionadas"
os.makedirs(output_folder, exist_ok=True)

new_width = 640
new_height = 640

def resize_image(image_path, output_image_path):

    image = cv2.imread(image_path)
    
    if image is None:
        print(f"Error al cargar la imagen {image_path}")
        return
    
 
    resized_image = cv2.resize(image, (new_width, new_height))


    cv2.imwrite(output_image_path, resized_image)
    print(f"Imagen redimensionada guardada en: {output_image_path}")

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(input_folder, filename)
        

        output_image_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_640.jpg")

        resize_image(image_path, output_image_path)

print(f"Todas las imágenes han sido redimensionadas a {new_width}x{new_height}.")
