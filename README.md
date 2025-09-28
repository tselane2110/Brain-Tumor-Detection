# Brain-Tumor-Detection

## 1. Dataset.py
* loads dataset from [Here.](https://www.kaggle.com/datasets/sartajbhuvaji/brain-tumor-classification-mri)
* resizes the whole dataset (training and testing) to 80x80 pixels
* performs data augmentation (only training data) by: #1 rotating each (original) image by 90 degrees, #2 flipping each (original) image vertically, so each image has one original copy, one rotated copy and one flipped copy.
