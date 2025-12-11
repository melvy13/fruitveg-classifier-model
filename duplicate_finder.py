from PIL import Image
import imagehash
import os

def find_duplicates(folder):
    hashes = {}
    duplicates = []

    for filename in os.listdir(folder):
        if filename.endswith(".jpg"):
            img = Image.open(os.path.join(folder, filename))
            h = imagehash.average_hash(img)
            if h in hashes:
                duplicates.append((filename, hashes[h]))
            else:
                hashes[h] = filename

    print(f"Possible duplicates in {folder}: {duplicates}")

find_duplicates(r"dataset\apple_ripe")
find_duplicates(r"dataset\apple_unripe")
find_duplicates(r"dataset\banana_ripe")
find_duplicates(r"dataset\banana_unripe")
find_duplicates(r"dataset\mango_ripe")
find_duplicates(r"dataset\mango_unripe")
find_duplicates(r"dataset\carrot_raw")
find_duplicates(r"dataset\carrot_cooked")
find_duplicates(r"dataset\broccoli_raw")
find_duplicates(r"dataset\broccoli_cooked")
