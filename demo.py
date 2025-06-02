from combine_multi_img_from_dir import create_image_grid
from cut_white_margin_img import trim_white_border



input_dir = r'C:\Users\xijia\Desktop\新建文件夹'
mid_pic = r'C:\Users\xijia\Desktop\新建文件夹.png'
output_pic = mid_pic


create_image_grid(input_dir, mid_pic, padding=10)
# trim_white_border(mid_pic, output_pic)
