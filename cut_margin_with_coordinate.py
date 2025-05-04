import os
from PIL import Image

# 要处理的目录
src_dir = r"C:\Users\xijia\Desktop\DoingPlatform\D20250417_继续教育项目结题\E01成果材料\5教学会议报告\1_ISAIE2024_教育人工智能国际会议分享报告"
# 裁剪区域：左、上、右、下
crop_box = (0, 0, 2000, 2850)

# 如果想把裁剪后的图另存至子目录，取消下面两行的注释：
# out_dir = os.path.join(src_dir, "cropped")
# os.makedirs(out_dir, exist_ok=True)

# 支持的图片后缀
exts = {".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".webp"}

for root, _, files in os.walk(src_dir):
    for fn in files:
        name, ext = os.path.splitext(fn)
        if ext.lower() in exts:
            src_path = os.path.join(root, fn)
            try:
                with Image.open(src_path) as im:
                    cropped = im.crop(crop_box)

                    # 覆盖原图：
                    cropped.save(src_path)
                    # ——或另存为新文件：
                    # out_path = os.path.join(out_dir, fn)
                    # cropped.save(out_path)

                    print(f"[OK] 裁剪并保存：{src_path}")
            except Exception as e:
                print(f"[ERR] 处理失败 {src_path}：{e}")
