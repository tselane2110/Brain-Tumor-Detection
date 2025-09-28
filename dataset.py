import kagglehub
import shutil

def download_dataset():
  path2data = kagglehub.dataset_download("sartajbhuvaji/brain-tumor-classification-mri")
  print("Path to dataset files:", path2data)
  return path2data
