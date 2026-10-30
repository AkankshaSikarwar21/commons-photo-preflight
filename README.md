# Commons Photo Preflight

**Commons Photo Preflight** is a Python command-line tool that helps Wikimedia Commons contributors check photographs before uploading them.

It performs basic quality and metadata checks so contributors can identify common upload problems early, such as low resolution, unsupported formats, missing camera metadata, excessive blur, or unclear filenames.

This project was created to support better-quality contributions to [Wikimedia Commons](https://commons.wikimedia.org/).

## Features

- Checks whether a file is a Commons-friendly image format
- Checks image resolution and estimated megapixels
- Detects potentially blurry images using Laplacian variance
- Reads EXIF metadata such as camera model, date taken, and GPS data
- Checks file size
- Suggests improvements for filenames
- Produces a simple PASS / WARNING / FAIL report
- Can check one image or every image in a folder

## Why This Project Matters

Wikimedia Commons accepts freely licensed media that is useful for educational purposes. Good images should have suitable resolution, clear descriptions, meaningful filenames, and appropriate license information. [Commons:Image guidelines](https://commons.wikimedia.org/wiki/Commons:Image_guidelines)

This tool does **not** upload files or decide copyright status automatically. Instead, it helps contributors catch technical issues before uploading.

## Supported Checks

| Check | Purpose |
|---|---|
| File format | Warns about formats that may not be ideal for Commons |
| Resolution | Warns if an image is below 2 megapixels |
| Blur detection | Flags images that may be out of focus |
| EXIF metadata | Shows camera, date, and GPS information when available |
| File size | Reports the size of the image |
| Filename quality | Warns about generic names such as `IMG_1234.jpg` |

Commons generally prefers photographs in JPEG format, while PNG is useful for diagrams, screenshots, and images requiring lossless quality. [Commons:First steps/Quality and description](https://commons.wikimedia.org/wiki/Commons:First_steps/Quality_and_description)

## Installation

Clone the repository:

```bash
git clone [https://github.com/AkankshaSikarwar21/commons-photo-preflight.git](https://github.com/AkankshaSikarwar21/commons-photo-preflight.git)
cd commons-photo-preflight
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Check one image:

```bash
python preflight.py photo.jpg
```

Check all images in a folder:

```bash
python preflight.py ./photos
```

Check an image and save the report:

```bash
python preflight.py photo.jpg --report report.txt
```

## Example Output

```text
Commons Photo Preflight Report
==============================

File: temple.jpg
Format: JPEG
Resolution: 4032 x 3024
Megapixels: 12.19 MP
File size: 3.4 MB
Blur score: 245.8

Checks:
[PASS] File format is suitable for Commons
[PASS] Resolution is above 2 megapixels
[PASS] Image does not appear blurry
[WARNING] No GPS location found in EXIF metadata
[FAIL] Filename is generic. Use a descriptive name such as 'madurai-meenakshi-temple-gopuram.jpg'

Overall result: NEEDS ATTENTION
```

## Example Good Filename

Instead of:

```text
IMG_20260323_114530.jpg
```

Use:

```text
madurai-meenakshi-temple-gopuram-2026.jpg
```

A meaningful filename makes files easier to search, identify, and reuse on Wikimedia projects. [106][116]

## Limitations

- The tool cannot automatically determine whether an image is freely licensed.
- It cannot verify whether a photograph is educational or within Commons scope.
- Blur detection is an estimate and should not replace human review.
- EXIF metadata may be removed by social-media platforms or image editors.

Commons requires files to be freely licensed or public domain, and the license and source must be clearly stated on the file description page. [111][112]

## Future Improvements

- Add a graphical user interface
- Check for duplicate images using perceptual hashing
- Suggest Commons categories using image recognition
- Generate a draft file description
- Integrate with the Wikimedia Commons API
- Add support for batch CSV metadata validation

## Tech Stack

- Python 3
- OpenCV
- Pillow
- NumPy

## License

This project is licensed under the MIT License.
