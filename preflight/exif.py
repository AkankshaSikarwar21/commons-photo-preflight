from PIL import Image, ExifTags


def check_exif(path):
    with Image.open(path) as img:
        exif = img.getexif()
        tags = {ExifTags.TAGS.get(k, k): v for k, v in exif.items()}
        tags.update(
            {ExifTags.TAGS.get(k, k): v for k, v in exif.get_ifd(0x8769).items()}
        )
        has_gps = bool(exif.get_ifd(0x8825))

    return {
        "has_date": "DateTimeOriginal" in tags or "DateTime" in tags,
        "has_camera": "Model" in tags,
        "has_gps": has_gps,
    }
