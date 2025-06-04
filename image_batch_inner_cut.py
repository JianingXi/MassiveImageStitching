import cv2
import numpy as np
import os

# 改为纯英文路径，避免中文导致imwrite失败
input_dir = r"C:\Users\xijia\Desktop\笨笨论文revision最终版\img_raw"
output_dir = "./output_crops2"  # 改成纯英文路径
os.makedirs(output_dir, exist_ok=True)

def read_image_robust(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    img_array = np.frombuffer(data, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    return img

def crop_image(img):
    print("原图像尺寸: ", img.shape)
    img_cropped_h = img[:, 150:2151]
    print("横向裁剪后尺寸: ", img_cropped_h.shape)
    rows = img_cropped_h.shape[0]
    keep_rows = [i for i in range(rows) if 220 <= i < 3100 or 3300 <= i < 3400]
    print("实际保留行数: ", len(keep_rows))
    if not keep_rows:
        return None
    img_cropped = img_cropped_h[keep_rows, :]
    print("最终裁剪后尺寸: ", img_cropped.shape)
    return img_cropped

idx = 1
for file in os.listdir(input_dir):
    if file.lower().endswith(".png"):
        file_path = os.path.join(input_dir, file)
        print("\n>>> 正在处理文件：", file)

        img = read_image_robust(file_path)
        if img is None:
            print("[WARNING] Cannot read:", file)
            continue

        cropped_img = crop_image(img)
        if cropped_img is None or cropped_img.size == 0:
            print("[WARNING] Cropped image empty:", file)
            continue

        output_filename = f"image_{idx}.png"
        output_path = os.path.join(output_dir, output_filename)
        save_success = cv2.imwrite(output_path, cropped_img)
        print("保存结果: ", save_success)

        idx += 1

print("\n[DONE] All images processed! Check:", output_dir)
