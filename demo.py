from combine_multi_img_from_dir import create_image_grid
from cut_white_margin_img import trim_white_border



input_dir = r'C:\Users\xijia\Desktop\D20240729_海南比赛新闻稿\比赛排名截图'
mid_pic = r'C:\Users\xijia\Desktop\D20240729_海南比赛新闻稿\output_image.jpg'
output_pic = r'C:\Users\xijia\Desktop\D20240729_海南比赛新闻稿\output_image.jpg'


create_image_grid(input_dir, mid_pic, padding=10)
trim_white_border(mid_pic, output_pic)
