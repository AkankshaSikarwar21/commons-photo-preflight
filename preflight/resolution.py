from PIL import Image


def get_resolution(path):
    with Image.open(path) as img:
        return img.size  # (width, height)


def is_low_resolution(path, min_pixels=2_000_000):
    width, height = get_resolution(path)
    return width * height < min_pixels
