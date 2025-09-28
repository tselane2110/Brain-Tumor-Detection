import kagglehub
import os
from PIL import Image

def download_dataset():
  path2data = kagglehub.dataset_download("sartajbhuvaji/brain-tumor-classification-mri")
  print("Path to dataset files:", path2data)
  return path2data

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
                    img = img.resize(size, Image.ANTIALIAS)
                    img.save(output_path)
                except Exception as e:
                    print(f"Error processing {input_path}: {e}")

    print(f"Resized images saved to: {output_dir}")

def main():
  path = download_dataset()
  resize_images(path+"/Training", "content/resized_dataset/training", size=(80, 80))
  resize_images(path+"/Testing", "content/resized_dataset/testing", size=(80, 80))

# to run main function
if __name__=="__main__":
    main()