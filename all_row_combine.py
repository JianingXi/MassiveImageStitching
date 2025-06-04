import os
import cv2
import numpy as np
from PIL import Image


def concatenate_images_horizontally(folder_path, output_path='output.jpg'):
    """
    修正颜色通道问题的图片拼接函数
    """
    # 获取图片文件列表
    image_files = [f for f in os.listdir(folder_path)
                   if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))]
    image_files.sort()

    if not image_files:
        print("文件夹中没有找到图片文件！")
        return

    # 读取图片并处理颜色通道
    images = []
    max_height = 0
    total_width = 0

    for img_file in image_files:
        img_path = os.path.join(folder_path, img_file)
        try:
            # 使用PIL读取（自动保持RGB顺序）
            pil_img = Image.open(img_path)

            # 转换为numpy数组并确保RGB顺序
            img = np.array(pil_img)

            # 处理不同颜色模式
            if img.ndim == 2:  # 灰度图
                img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            elif img.shape[2] == 4:  # RGBA
                img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
            elif img.shape[2] == 3:  # RGB
                pass  # 已经是RGB顺序，无需转换

            h, w = img.shape[:2]
            max_height = max(max_height, h)
            total_width += w
            images.append(img)
            print(f"成功加载: {img_file} (尺寸: {w}x{h})")
        except Exception as e:
            print(f"无法读取图片 {img_file}: {str(e)}")
            continue

    if not images:
        print("没有有效的图片可拼接！")
        return

    # 创建空白RGB画布
    result = np.zeros((max_height, total_width, 3), dtype=np.uint8)

    # 拼接图片
    x_offset = 0
    for img in images:
        h, w = img.shape[:2]
        result[0:h, x_offset:x_offset + w] = img
        x_offset += w

    # 保存时明确指定颜色通道顺序
    cv2.imwrite(output_path, cv2.cvtColor(result, cv2.COLOR_RGB2BGR))
    print(f"\n拼接完成！输出文件: {os.path.abspath(output_path)}")
    print(f"最终尺寸: 宽度 {total_width}px, 高度 {max_height}px")


if __name__ == "__main__":
    folder_path = r"C:\Users\xijia\Desktop\笨笨论文revision最终版\output_crops2"
    output_path = "./comfig02.jpg"

    if not os.path.exists(folder_path):
        print(f"错误：文件夹不存在 - {folder_path}")
    else:
        concatenate_images_horizontally(folder_path, output_path)