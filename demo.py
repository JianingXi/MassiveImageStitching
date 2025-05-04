from combine_multi_img_from_dir import create_image_grid
from cut_white_margin_img import trim_white_border



input_dir = r'C:\Users\xijia\Desktop\DoingPlatform\D20250417_继续教育项目结题\E01成果材料\4教改论文发表_pic\论文2_办公自动化_国家级期刊_中国核心期刊遴选数据库\3正文'
mid_pic = r'C:\Users\xijia\Desktop\DoingPlatform\D20250417_继续教育项目结题\E01成果材料\4教改论文发表_pic\论文2_办公自动化_国家级期刊_中国核心期刊遴选数据库\3正文all.png'
output_pic = mid_pic


create_image_grid(input_dir, mid_pic, padding=10)
trim_white_border(mid_pic, output_pic)
