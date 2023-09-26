from PIL import Image
import os

PATH = 'static/img'


def compress(path, img_name):
    file_path = f"{path}/{img_name}"
    image = Image.open(file_path)
    width, height = image.size
    size_kb = os.path.getsize(file_path)
    new_size = ()
    if size_kb < 400000:
        new_size = (width - 50, height - 50)
    if size_kb >= 400000:
        new_size = (width // 2, height // 2)

    resized_image = image.resize(new_size)
    resized_image.save(file_path,
                       optimize=True,
                       quality=100,
                       irreversible=True)

    return


img_directory = os.listdir(PATH)
images = []
for item in img_directory:
    try:
        with Image.open(f'{PATH}/{item}') as img:
            size = os.path.getsize(f'{PATH}/{item}')
            if size > 100000:
                images.append(item)
    except OSError:
        pass
print(images)

for img in images:
    while os.path.getsize(f'{PATH}/{img}') > 100000:
        compress(PATH, img)
