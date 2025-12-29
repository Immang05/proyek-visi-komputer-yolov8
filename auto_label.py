from ultralytics import YOLO
import os

# Load model pretrained
model = YOLO("yolov8n.pt")

# Folder input
image_dir = r"C:\Users\PLN\dataset\images"
label_dir = r"C:\Users\PLN\dataset\labels"

os.makedirs(label_dir, exist_ok=True)

# Jalankan deteksi
results = model.predict(
    source=image_dir,
    save=False,
    save_txt=True,
    conf=0.4
)

print("Auto-label selesai!")
