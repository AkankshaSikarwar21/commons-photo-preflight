import cv2


def blur_score(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"Cannot read image: {path}")
    return cv2.Laplacian(img, cv2.CV_64F).var()


def is_blurry(path, threshold=100.0):
    return blur_score(path) < threshold


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python blur.py <image_path>")
        sys.exit(1)

    path = sys.argv[1]
    print("Blur score:", blur_score(path))
    print("Blurry:", is_blurry(path))