
# Python Utility Scripts

This repository contains three Python scripts for various utility purposes: directory summary generation, image combination, and image margin cutting.

本仓库包含三个用于不同实用目的的Python脚本：目录摘要生成、图像合并和图像边距裁剪。

## Scripts

### 1. Directory Summary Script

Generates a summary of the contents of a specified directory and saves it to a text file.

生成指定目录内容的摘要，并将其保存到文本文件中。

**Script:** `get_directory_summary_txt.py`

**Features:**
- Lists all files and directories in the specified directory.
- Saves the summary to a text file.
- 简单易用，只需指定目录路径。

**Usage:**
1. Modify the script to specify the directory you want to summarize:
    ```python
    directory_path = r'C:\path\to\your\directory'
    ```
2. Run the script:
    ```sh
    python get_directory_summary_txt.py
    ```
3. The summary will be saved to `directory_summary.txt` in the specified directory.

**Code:**
```python
import os

def get_directory_summary(directory_path):
    summary = []
    for root, dirs, files in os.walk(directory_path):
        summary.append(f"Directory: {root}")
        for dir in dirs:
            summary.append(f"  Subdirectory: {dir}")
        for file in files:
            summary.append(f"  File: {file}")
    return "\n".join(summary)

def save_summary_to_file(summary, file_path):
    with open(file_path, 'w') as file:
        file.write(summary)

if __name__ == "__main__":
    directory_path = r'C:\path\to\your\directory'  # 修改为你的目录路径
    summary_file_path = os.path.join(directory_path, 'directory_summary.txt')
    summary = get_directory_summary(directory_path)
    save_summary_to_file(summary, summary_file_path)
    print(f"Directory summary saved to {summary_file_path}")
```

### 2. Combine Multiple Images from Directory

Combines multiple images from a specified directory into a single image.

将指定目录中的多个图像合并为一个图像。

**Script:** `combine_multi_img_from_dir.py`

**Features:**
- Combines all images in the specified directory into one image.
- 支持多种图像格式。

**Usage:**
1. Modify the script to specify the directory containing the images:
    ```python
    folder_path = r'C:\path\to\your\directory'
    ```
2. Run the script:
    ```sh
    python combine_multi_img_from_dir.py
    ```
3. The combined image will be saved in the specified directory.

**Code:**
```python
import os
from PIL import Image

def combine_images(folder_path):
    images = [Image.open(os.path.join(folder_path, f)) for f in os.listdir(folder_path) if f.lower().endswith(('png', 'jpg', 'jpeg', 'bmp'))]
    widths, heights = zip(*(i.size for i in images))
    total_width = sum(widths)
    max_height = max(heights)
    
    combined_image = Image.new('RGB', (total_width, max_height))
    
    x_offset = 0
    for img in images:
        combined_image.paste(img, (x_offset, 0))
        x_offset += img.width

    combined_image_path = os.path.join(folder_path, 'combined_image.png')
    combined_image.save(combined_image_path)
    print(f"Combined image saved to {combined_image_path}")

if __name__ == "__main__":
    folder_path = r'C:\path\to\your\directory'  # 修改为你的目录路径
    combine_images(folder_path)
```

### 3. Cut White Margin from Image

Cuts the white margin from an image.

裁剪图像中的白色边距。

**Script:** `cut_white_margin_img.py`

**Features:**
- Detects and removes white margins from an image.
- 适用于多种图像格式。

**Usage:**
1. Modify the script to specify the image file path:
    ```python
    image_path = r'C:\path\to\your\image.png'
    ```
2. Run the script:
    ```sh
    python cut_white_margin_img.py
    ```
3. The processed image will be saved in the same directory.

**Code:**
```python
from PIL import Image
import numpy as np

def cut_white_margin(image_path):
    image = Image.open(image_path)
    image_np = np.array(image)
    
    # Assuming the image has an alpha channel, convert it to RGB
    if image_np.shape[2] == 4:
        image_np = image_np[:, :, :3]
    
    # Find the bounding box of non-white areas
    mask = (image_np[:, :, 0:3] != [255, 255, 255]).any(2)
    coords = np.argwhere(mask)
    y0, x0 = coords.min(axis=0)
    y1, x1 = coords.max(axis=0) + 1
    
    # Crop the image to the bounding box
    cropped_image = image.crop((x0, y0, x1, y1))
    
    cropped_image_path = os.path.join(os.path.dirname(image_path), 'cropped_' + os.path.basename(image_path))
    cropped_image.save(cropped_image_path)
    print(f"Cropped image saved to {cropped_image_path}")

if __name__ == "__main__":
    image_path = r'C:\path\to\your\image.png'  # 修改为你的图像文件路径
    cut_white_margin(image_path)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 许可证

这个项目是根据MIT许可证授权的 - 详见[LICENSE](LICENSE)文件。
