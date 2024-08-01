from PIL import Image
import os
import math


def get_all_images(image_folder):
    """递归获取文件夹及其子文件夹中的所有图片文件"""
    image_files = []
    for root, _, files in os.walk(image_folder):
        for file in files:
            if file.lower().endswith(('png', 'jpg', 'jpeg')):
                image_files.append(os.path.join(root, file))
    return image_files


def closest_factors(n):
    """找到最接近的两个整数因子，使它们的乘积等于或接近于n"""
    root = int(math.sqrt(n))
    for i in range(root, 0, -1):
        if n % i == 0:
            return i, n // i
    return root, (n + root - 1) // root  # 调整为非因数情况


def create_image_grid(image_folder, output_image, max_dim=65500, padding=10):
    try:
        # 获取所有图片文件
        image_files = get_all_images(image_folder)
        image_files.sort()  # 对文件进行排序以保持顺序

        if len(image_files) == 0:
            raise ValueError("No image files found in the specified directory and its subdirectories.")

        print(f"Found {len(image_files)} images.")
        for img in image_files:
            print(f"Image file: {img}")

        images = [Image.open(img) for img in image_files]

        # 调整所有图像到相同的大小
        widths, heights = zip(*(i.size for i in images))
        max_width, max_height = max(widths), max(heights)

        # 如果单个图像尺寸过大，缩小图像尺寸
        if max_width * max_height > max_dim:
            scale_factor = math.sqrt(max_dim / (max_width * max_height))
            max_width = int(max_width * scale_factor)
            max_height = int(max_height * scale_factor)

        images = [img.resize((max_width, max_height)) for img in images]

        # 计算最接近的网格尺寸
        num_images = len(images)
        grid_rows, grid_cols = closest_factors(num_images)

        # 计算输出图像的尺寸
        total_width = grid_cols * max_width + (grid_cols - 1) * padding
        total_height = grid_rows * max_height + (grid_rows - 1) * padding

        # 如果输出图像尺寸超过最大限制，调整网格尺寸
        while total_width > max_dim or total_height > max_dim:
            if total_width > total_height:
                grid_cols += 1
            else:
                grid_rows += 1
            total_width = grid_cols * max_width + (grid_cols - 1) * padding
            total_height = grid_rows * max_height + (grid_rows - 1) * padding

        new_image = Image.new('RGB', (total_width, total_height), 'white')

        # 将图像粘贴到表格中
        for i, img in enumerate(images):
            row = i // grid_cols
            col = i % grid_cols
            x = col * (max_width + padding)
            y = row * (max_height + padding)
            new_image.paste(img, (x, y))

        new_image.save(output_image)
        print(f"Image grid saved as {output_image}")

    except Exception as e:
        print(f"An error occurred: {e}")

