from combine_multi_img_from_dir import create_image_grid
from cut_white_margin_img import trim_white_border



input_dir = r'C:\Users\xijia\Downloads\思政案例\test4'
mid_pic = r'C:\Users\xijia\Downloads\思政案例\test444.png'
output_pic = mid_pic


create_image_grid(input_dir, mid_pic, padding=10)
trim_white_border(mid_pic, output_pic)
