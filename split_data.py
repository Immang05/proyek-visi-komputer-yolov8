import os
import random
import shutil

img_src = "images/all"
lbl_src = "labels/all"

train_img = "images/train"
val_img = "images/val"
train_lbl = "labels/train"
val_lbl = "labels/val"

for d in [train_img, val_img, train_lbl, val_lbl]:
    os.makedirs(d, exist_ok=True)

images = [f for f in os.listdir(img_src) if f.endswith(".jpg")]
random.shuffle(images)

split = int(0.8 * len(images))

for i, img in enumerate(images):
    src_img = os.path.join(img_src, img)
    src_lbl = os.path.join(lbl_src, img.replace(".jpg", ".txt"))

    if i < split:
        shutil.copy(src_img, train_img)
        shutil.copy(src_lbl, train_lbl)
    else:
        shutil.copy(src_img, val_img)
        shutil.copy(src_lbl, val_lbl)

print("Split dataset selesai dan AMAN")
