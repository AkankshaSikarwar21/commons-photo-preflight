import argparse
import csv
import os

from preflight.blur import blur_score
from preflight.resolution import get_resolution
from preflight.exif import check_exif

EXTENSIONS = (".jpg", ".jpeg", ".png", ".tif", ".tiff")
BLUR_THRESHOLD = 100.0
MIN_PIXELS = 2_000_000


def check_photo(path):
    problems, warnings = [], []

    score = blur_score(path)
    if score < BLUR_THRESHOLD:
        problems.append("blurry")

    width, height = get_resolution(path)
    if width * height < MIN_PIXELS:
        problems.append("low resolution")

    exif = check_exif(path)
    if not exif["has_date"]:
        warnings.append("no date")
    if not exif["has_camera"]:
        warnings.append("no camera info")
    if not exif["has_gps"]:
        warnings.append("no GPS")

    status = "FAIL" if problems else ("WARN" if warnings else "PASS")
    return {
        "file": os.path.basename(path),
        "status": status,
        "blur_score": round(score, 1),
        "size": f"{width}x{height}",
        "problems": "; ".join(problems),
        "warnings": "; ".join(warnings),
    }


def main():
    parser = argparse.ArgumentParser(description="Check photos before Commons upload")
    parser.add_argument("folder", help="Folder containing photos")
    parser.add_argument("--report", default="report.csv", help="CSV output file")
    args = parser.parse_args()

    rows = []
    for name in sorted(os.listdir(args.folder)):
        if not name.lower().endswith(EXTENSIONS):
            continue
        path = os.path.join(args.folder, name)
        try:
            row = check_photo(path)
        except Exception as e:
            row = {"file": name, "status": "ERROR", "blur_score": "",
                   "size": "", "problems": str(e), "warnings": ""}
        rows.append(row)
        print(f"{row['status']:5} {row['file']}  {row['problems']} {row['warnings']}")

    if rows:
        with open(args.report, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
        print(f"\nChecked {len(rows)} photos. Report saved to {args.report}")
    else:
        print("No photos found in that folder.")


if __name__ == "__main__":
    main()
    