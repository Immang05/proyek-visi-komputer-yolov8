import glob

files = glob.glob("labels/train/*.txt") + glob.glob("labels/val/*.txt")

for f in files:
    with open(f, "r") as file:
        lines = file.readlines()

    new_lines = []
    for line in lines:
        parts = line.strip().split()
        parts[0] = "0"   # ganti class jadi 0
        new_lines.append(" ".join(parts) + "\n")

    with open(f, "w") as file:
        file.writelines(new_lines)

print("Semua label berhasil diperbaiki ✅")
