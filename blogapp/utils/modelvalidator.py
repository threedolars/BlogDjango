from django.core.exceptions import ValidationError


def validate_image(image):
    if not image.name.lower().endswith('.png'):
        raise ValidationError('The image needs to be a png archive')
