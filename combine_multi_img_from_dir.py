from PIL import Image
import os


def get_all_images(image_folder):
    """递归获取文件夹及其子文件夹中的所有图片文件"""
    image_files = []
    for root, _, files in os.walk(image_folder):
        for file in files:
            if file.lower().endswith(('png', 'jpg', 'jpeg')):
                image_files.append(os.path.join(root, file))
    return image_files


def create_image_grid(image_folder, output_image, grid_size=(5, 5), padding=10):
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
        images = [img.resize((max_width, max_height)) for img in images]

        # 计算输出图像的尺寸
        total_width = grid_size[1] * max_width + (grid_size[1] - 1) * padding
        total_height = grid_size[0] * max_height + (grid_size[0] - 1) * padding

        new_image = Image.new('RGB', (total_width, total_height), 'white')

        # 将图像粘贴到表格中
        for i, img in enumerate(images):
            row = i // grid_size[1]
            col = i % grid_size[1]
            x = col * (max_width + padding)
            y = row * (max_height + padding)
            new_image.paste(img, (x, y))

        new_image.save(output_image)
        print(f"Image grid saved as {output_image}")

    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage:
create_image_grid(r'C:\Users\DELL\Desktop\B教学_教学与人才培养_B10_本科班主任_生工22级班主任_2024\04日常留痕', 'output_image.jpg', grid_size=(5, 5), padding=10)
