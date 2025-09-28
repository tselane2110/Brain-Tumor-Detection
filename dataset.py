#import kagglehub
import os
from PIL import Image

"""
# in case we want to download the dataset from kaggle
def download_dataset():
  path2data = kagglehub.dataset_download("sartajbhuvaji/brain-tumor-classification-mri")
  print("Path to dataset files:", path2data)
  return path2data
"""

def resize_images(input_dir, output_dir, size=(80, 80)):
    """
    Resize all images in input_dir (with subfolders for classes)
    and save them in output_dir with the same folder structure.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                # Full input path
                input_path = os.path.join(root, file)

                # Create corresponding output path
                relative_path = os.path.relpath(root, input_dir)
                output_folder = os.path.join(output_dir, relative_path)
                os.makedirs(output_folder, exist_ok=True)
                output_path = os.path.join(output_folder, file)

                # Resize and save
                try:
                    img = Image.open(input_path)
                    img = img.resize(size, Image.Resampling.LANCZOS)
                    img.save(output_path)
                except Exception as e:
                    print(f"Error processing {input_path}: {e}")

    print(f"Resized images saved to: {output_dir}")

def augment_images(input_dir, output_dir):
    """
    For each image in input_dir, create two augmentations:
    1. Rotated 90 degrees
    2. Flipped vertically
    Save them in output_dir with the same folder structure.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                input_path = os.path.join(root, file)

                # Create corresponding output path
                relative_path = os.path.relpath(root, input_dir)
                output_folder = os.path.join(output_dir, relative_path)
                os.makedirs(output_folder, exist_ok=True)

                # Load image
                try:
                    img = Image.open(input_path)

                    # Save original (optional, if you want a full copy)
                    # img.save(os.path.join(output_folder, file))

                    # 1. Rotation (90 degrees)
                    rotated = img.rotate(90, expand=True)
                    rotated.save(os.path.join(output_folder, f"{os.path.splitext(file)[0]}_rot90.jpg"))

                    # 2. Flip vertically
                    flipped = img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
                    flipped.save(os.path.join(output_folder, f"{os.path.splitext(file)[0]}_flipV.jpg"))

                except Exception as e:
                    print(f"Error processing {input_path}: {e}")

    print(f"Augmented images saved in: {output_dir}")

def main():
  # path = download_dataset()
  path = "dataset"
  output_path = "resized_dataset"
  resize_images(path+"/Training", output_path+"/Training", size=(80, 80))
  resize_images(path+"/Testing", output_path+"/Testing", size=(80, 80))
  augment_images("dataset/Training", "dataset/Training")
  augment_images("dataset/Testing", "dataset/Testing")

# to run main function
if __name__=="__main__":
    main()