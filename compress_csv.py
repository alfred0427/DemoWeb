import os
import gzip
import shutil

DATA_DIR = "public/data"

for filename in os.listdir(DATA_DIR):
    if filename.endswith(".csv"):
        csv_path = os.path.join(DATA_DIR, filename)
        gz_path = csv_path + ".gz"

        if os.path.exists(gz_path):
            print(f"✔ 已存在：{gz_path}，略過")
            continue

        with open(csv_path, "rb") as f_in:
            with gzip.open(gz_path, "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)

        print(f"✅ 壓縮完成：{gz_path}")
