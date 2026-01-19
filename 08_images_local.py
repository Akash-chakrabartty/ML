# 08_images_local.py
import cv2
import glob

# Put some images in an "images" folder first
image_paths = glob.glob("images/*.jpg")  # or *.png
print("Found files:", image_paths)

images = []
for path in image_paths:
    img = cv2.imread(path)
    if img is not None:
        print(f"{path}: shape={img.shape}")
        images.append(img)
    else:
        print(f"Could not read {path}")

print(f"\nTotal images loaded: {len(images)}")
