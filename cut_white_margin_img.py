from PIL import Image, ImageChops, ImageFile

Image.MAX_IMAGE_PIXELS = None  # 禁用Pillow的像素限制
ImageFile.LOAD_TRUNCATED_IMAGES = True


def resize_image_if_needed(image):
    """
    如果图像的像素数超过阈值，缩小图像。
    :param image: PIL Image对象
    :return: 缩小后的PIL Image对象
    """
    max_pixels = 178956970
    if image.size[0] * image.size[1] > max_pixels:
        scaling_factor = (max_pixels / (image.size[0] * image.size[1])) ** 0.5
        new_size = (int(image.size[0] * scaling_factor), int(image.size[1] * scaling_factor))
        return image.resize(new_size, Image.LANCZOS)
    return image


def trim_white_border(image_path, output_path):
    """
    裁剪图片最外圈的白边并保存结果
    :param image_path: 输入图片的路径
    :param output_path: 输出图片的路径
    """
    try:
        # 打开图像
        with Image.open(image_path) as img:
            # 如果需要，调整图像大小
            img = resize_image_if_needed(img)

            # 转换为灰度图像
            gray_image = img.convert("L")

            # 创建一个与原图像尺寸相同的白色背景图像
            bg = Image.new("L", gray_image.size, 255)

            # 使用ImageChops.difference计算差异图像
            diff = ImageChops.difference(gray_image, bg)

            # 获取差异图像的边界框
            bbox = diff.getbbox()

            if bbox:
                # 裁剪图像并保存
                trimmed_image = img.crop(bbox)
                trimmed_image.save(output_path)
                print(f"Trimmed image saved as {output_path}")
            else:
                print("No white border found, image remains unchanged.")

    except Exception as e:
        print(f"An error occurred: {e}")


