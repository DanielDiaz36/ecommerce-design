from PIL import Image
from io import BytesIO
from django.core.files import File

def compress_image(image):
    im = Image.open(image)
    # im = im.convert('RGB')
    out = BytesIO()
    # im.save(out, 'JPEG', name=image.name, optimize=True, quality=70)
    im.save(out, quality=70)
    compressed = File(out, name=image.name)
    im.close()
    return compressed