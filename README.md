# Commons Photo Preflight

A small Python command-line tool that checks photos before they are uploaded to [Wikimedia Commons](https://commons.wikimedia.org/). It helps contributors catch common problems early, such as blurry or low-resolution images and missing metadata.

It was built for photo-walk participants of Wiki Club SATI, and it is a beginner project that is still growing.

## What it checks today

- **Blur:** estimated using the variance of the Laplacian (OpenCV)
- **Resolution:** flags images below 2 megapixels
- **EXIF metadata:** reports whether date, camera model, and GPS data are present

Each photo gets a status: `PASS`, `WARN`, or `FAIL`. Results are also saved to `report.csv`.

## Install

```
git clone https://github.com/AkankshaSikarwar21/commons-photo-preflight.git
cd commons-photo-preflight
pip install -r requirements.txt
```

## Usage

Check every photo in a folder:

```
python -m preflight.cli "C:\path\to\photos"
```

## Example output

```
PASTE YOUR REAL OUTPUT HERE
```

## Limitations

- Blur detection is an estimate. Scores differ between cameras, so the threshold may need adjusting.
- Photos edited or shared through social media often lose EXIF data.
- The tool does not check licensing or whether an image is in scope for Commons. Always review those yourself.
- Currently it works on folders only.

## Planned

- Commons duplicate check using the file's SHA-1 hash
- Configurable thresholds in a `config.yaml` file
- File size and format checks
- Filename suggestions
- Automated tests

## Tech stack

Python 3, OpenCV, Pillow, NumPy

## Author

Akanksha Sikarwar (Wikimedia user: [Imakanksha](https://meta.wikimedia.org/wiki/User:Imakanksha)), board member of Wiki Club SATI.

## License

MIT
