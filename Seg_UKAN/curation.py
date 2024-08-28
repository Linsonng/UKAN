import os
import shutil

# Define the path to your folder
folder_path = 'Dataset_BUSI_with_GT/malignant'

# Create directories for images and masks
images_dir = os.path.join('Dataset_BUSI_with_GT/malignant_images')
masks_dir = os.path.join('Dataset_BUSI_with_GT/malignant_masks')

os.makedirs(images_dir, exist_ok=True)
os.makedirs(masks_dir, exist_ok=True)

# Iterate over the files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.png'):
        if '_mask' in file_name:
            # Move mask files to the masks directory
            shutil.move(os.path.join(folder_path, file_name), os.path.join(masks_dir, file_name))
        else:
            # Move image files to the images directory
            shutil.move(os.path.join(folder_path, file_name), os.path.join(images_dir, file_name))

print("Files have been reorganized successfully!")
