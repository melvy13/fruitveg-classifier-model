import random
import shutil
import os

image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp', 'avif')

def pick_random_images(src_folder, dst_folder, n=100):
    os.makedirs(dst_folder, exist_ok=True)

    # Get all image files in the source folder
    all_images = [f for f in os.listdir(src_folder) if f.lower().endswith(image_extensions)]

    if not all_images:
        print("No image files found in the source folder.")
        return
    
    num_to_pick = min(n, len(all_images))

    selected_images = random.sample(all_images, num_to_pick)

    for filename in selected_images:
        src_path = os.path.join(src_folder, filename)
        dst_path = os.path.join(dst_folder, filename)
        shutil.copy2(src_path, dst_path)

    print(f"{num_to_pick} images copied from '{src_folder}' to '{dst_folder}'.")


# Organize Mango Banana Dataset first
mango_banana_dirs = [
    r"Mango_Banana_Dataset\data\test\images",
    r"Mango_Banana_Dataset\data\train\images"
]

mb_categories = ["banana_ripe", "banana_unripe", "mango_ripe", "mango_unripe"]
counters = {category: 1 for category in mb_categories}

for category in mb_categories:
    os.makedirs(os.path.join("temporary_folder", category), exist_ok=True)

print("Sorting Mango Banana dataset...")

for dir in mango_banana_dirs:
    for filename in os.listdir(dir):
        if filename.lower().endswith(image_extensions):
            source_path = os.path.join(dir, filename)

            if filename.startswith('Ripe_Banana'):
                category = 'banana_ripe'
            elif filename.startswith('Raw_Banana'):
                category = 'banana_unripe'
            elif filename.startswith('Ripe_Mango'):
                category = 'mango_ripe'
            elif filename.startswith('Raw_Mango'):
                category = 'mango_unripe'
            else:
                continue

            new_filename = f'{category}_{counters[category]}{os.path.splitext(filename)[1]}'
            destination_path = os.path.join("temporary_folder", category, new_filename)

            shutil.copy2(source_path, destination_path)
            counters[category] += 1

print("Image organization complete (Mango Banana Dataset)")

pick_random_images(r"temporary_folder\mango_ripe", r"dataset\mango_ripe")
pick_random_images(r"temporary_folder\mango_unripe", r"dataset\mango_unripe")
pick_random_images(r"temporary_folder\banana_ripe", r"dataset\banana_ripe")
pick_random_images(r"temporary_folder\banana_unripe", r"dataset\banana_unripe")
shutil.rmtree("temporary_folder")

pick_random_images(r"vegfru\apple", r"dataset\apple_ripe")
pick_random_images(r"vegfru\green_apple", r"dataset\apple_unripe")
pick_random_images(r"vegfru\banana", r"dataset\banana_ripe")

# Unused as vegfru\mango mixes both ripe & unripe mangoes
# pick_random_images(r"vegfru\mango", r"dataset\mango_ripe")

pick_random_images(r"Vegetable Images\test\Broccoli", r"dataset\broccoli_raw", 50)
pick_random_images(r"Vegetable Images\train\Broccoli", r"dataset\broccoli_raw", 50)
pick_random_images(r"Vegetable Images\validation\Broccoli", r"dataset\broccoli_raw", 50)
pick_random_images(r"Vegetable Images\test\Carrot", r"dataset\carrot_raw", 50)
pick_random_images(r"Vegetable Images\train\Carrot", r"dataset\carrot_raw", 50)
pick_random_images(r"Vegetable Images\validation\Carrot", r"dataset\carrot_raw", 50)
