from PIL import Image
import os

input_folder = "C:\\Users\\LENOVO\\Downloads\\блок1"
output_folder = "C:\\Users\\LENOVO\\Downloads\\блок2"

crop_left = 30  # Кількість пікселів для обрізки зліва
crop_top = 0  # Кількість пікселів для обрізки зверху
crop_right = 30  # Кількість пікселів для обрізки справа
crop_bottom = 0  # Кількість пікселів для обрізки знизу

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        with Image.open(os.path.join(input_folder, filename)) as img:
            width, height = img.size
            cropped_img = img.crop((crop_left, crop_top, width - crop_right, height - crop_bottom))
            cropped_img.save(os.path.join(output_folder, filename))
print("Обрізка завершена.")