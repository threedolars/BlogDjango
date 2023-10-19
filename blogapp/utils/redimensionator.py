from django.conf import settings
from pathlib import Path
from PIL import Image


def rezize_image(image_django, new_width=800, optmize=True, quality=60):
    image_path = Path(settings.MEDIA_ROOT / image_django.name).resolve()
    image_pillow = Image.open(image_django)
    original_width, original_height = image_pillow.size

    if original_width <= new_width:
        image_pillow.close()
        return image_pillow

    new_height = round(new_width * original_height / original_width)

    new_image = image_pillow.resize((new_width, new_height), Image.LANCZOS)

    new_image.save(image_path, optimize=optmize, quality=quality)

    return new_image
