import os

def rename_images(folder_path, base_name):
    files = os.listdir(folder_path)
    image_files = [f for f in files if f.lower().endswith('.jpg')]

    for i, filename in enumerate(image_files, start=1):

        ext = os.path.splitext(filename)[1]
        new_name = f"{base_name}_{i}{ext}"
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)
        print(f"Renamed: {filename} → {new_name}")

    print(f"All images for {base_name} renamed.")

# temporary rename to prevent possibility of name conflicts
def temp_rename(folder_path):
    files = os.listdir(folder_path)
    image_files = [f for f in files if f.lower().endswith('.jpg')]

    for i, filename in enumerate(image_files, start=1):
        old_path = os.path.join(folder_path, filename)
        temp_name = f"temp_{i}{os.path.splitext(filename)[1]}"
        temp_path = os.path.join(folder_path, temp_name)
        os.rename(old_path, temp_path)

    print(f"{folder_path} renamed temporarily")

#temp_rename(r"dataset2\carrot_cooked")
#temp_rename(r"dataset2\broccoli_cooked")
temp_rename(r"dataset2\carrot_raw")
temp_rename(r"dataset2\broccoli_raw")
temp_rename(r"dataset2\banana_unripe")
temp_rename(r"dataset2\banana_ripe")
temp_rename(r"dataset2\mango_ripe")
temp_rename(r"dataset2\mango_unripe")
temp_rename(r"dataset2\apple_ripe")
temp_rename(r"dataset2\apple_unripe")

#rename_images(r"dataset2\carrot_cooked", "carrot_cooked")
#rename_images(r"dataset2\broccoli_cooked", "broccoli_cooked")
rename_images(r"dataset2\carrot_raw", "carrot_raw")
rename_images(r"dataset2\broccoli_raw", "broccoli_raw")
rename_images(r"dataset2\banana_unripe", "banana_unripe")
rename_images(r"dataset2\banana_ripe", "banana_ripe")
rename_images(r"dataset2\mango_ripe", "mango_ripe")
rename_images(r"dataset2\mango_unripe", "mango_unripe")
rename_images(r"dataset2\apple_ripe", "apple_ripe")
rename_images(r"dataset2\apple_unripe", "apple_unripe")