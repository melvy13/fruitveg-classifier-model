from PIL import Image
import pillow_avif
import os

def convert_to_jpg(input_path, output_path=None):

    if output_path is None:
        base = os.path.splitext(input_path)[0]
        output_path = base + ".jpg"

    try:
        with Image.open(input_path) as img:
            img = img.convert("RGB")
            img.save(output_path, "JPEG", quality=95)
            print(f"Converted {input_path} to {output_path}")

    except Exception as e:
        print(f"Failed to convert: {e}")

# Example usage
# convert_to_jpg("testimage.webp")
# convert_to_jpg("testimage.png")
# convert_to_jpg("testimage.avif")
