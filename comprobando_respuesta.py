import cv2

def read_annotations(txt_file):
    boxes = []
    with open(txt_file, 'r') as f:
        for line in f.readlines():
            parts = line.strip().split()
            class_id = float(parts[0]) 
            x_center = float(parts[1])
            y_center = float(parts[2])
            w = float(parts[3])
            h = float(parts[4])
            boxes.append((class_id, x_center, y_center, w, h))
    return boxes


def draw_box(image, x_center, y_center, w, h, color=(0, 255, 0), thickness=2):
    x_min = int((x_center - w / 2) * image.shape[1])
    y_min = int((y_center - h / 2) * image.shape[0])
    x_max = int((x_center + w / 2) * image.shape[1])
    y_max = int((y_center + h / 2) * image.shape[0])
    cv2.rectangle(image, (x_min, y_min), (x_max, y_max), color, thickness)
    return image


def draw_arrow(image, x_center, y_center, w, h, color=(0, 0, 255), thickness=2):
    start_point = (int(x_center * image.shape[1]), int(y_center * image.shape[0]))
    end_point = (int(x_center * image.shape[1]), int((y_center + 0.1) * image.shape[0]))  # Apuntando hacia abajo
    cv2.arrowedLine(image, start_point, end_point, color, thickness)
    return image


input_image_path = r"/home/ariel/github_repos/reconocimiento_paquetes/imagenes_aumentadas/IMG_9102_640_aug_bg21.jpg"
txt_file_path = r"/home/ariel/github_repos/reconocimiento_paquetes/labels_aumentadas/IMG_9102_640_aug_bg21.txt"

image = cv2.imread(input_image_path)

boxes = read_annotations(txt_file_path)


for box in boxes:
    class_id, x_center, y_center, w, h = box


    if class_id == 0.0 or 1.0:
        image = draw_box(image, x_center, y_center, w, h)
    

    elif class_id == 2:
        image = draw_arrow(image, x_center, y_center, w, h)


cv2.imshow("Image with Boxes and Arrows", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imwrite("output_image.jpg", image)
