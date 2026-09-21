import sys
import os
from PIL import Image

def is_red_pixel(r, g, b):
    # Detect prominent red shades
    return r > 120 and r > 1.4 * g and r > 1.4 * b

def check_image(image_path: str) -> str:
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"File not found: {image_path}")

    with Image.open(image_path) as img:
        img_rgb = img.convert("RGB")
        width, height = img_rgb.size
        total_pixels = width * height

        if total_pixels == 0:
            return "OK"

        # Count defect (red) pixels
        defect_pixels = 0
        pixels = img_rgb.getdata()
        for r, g, b in pixels:
            if is_red_pixel(r, g, b):
                defect_pixels += 1

        # If more than 0.5% of pixels are red, consider it DEFECT
        defect_ratio = defect_pixels / total_pixels
        if defect_ratio > 0.005:
            return "DEFECT"
        else:
            return "OK"

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_image>")
        sys.exit(1)

    image_path = sys.argv[1]
    result = check_image(image_path)
    print(result)

if __name__ == "__main__":
    main()
