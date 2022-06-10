'''
Description: 
Author: JinShiyin
Email: shiyinjin@foxmail.com
Date: 2022-02-18 16:53:54
'''
import os
import shutil

style_2_image_name = {u'berthe-morisot': u'Morisot-1886-the-lesson-in-the-garden',
		      u'claude-monet': u'monet-1914-water-lilies-37.jpg!HD',
		      u'edvard-munch': u'Munch-the-scream-1893',
		      u'el-greco': u'el-greco-the-resurrection-1595.jpg!HD',
		      u'ernst-ludwig-kirchner': u'Kirchner-1913-street-berlin.jpg!HD',
		      u'jackson-pollock': u'Pollock-number-one-moma-November-31-1950-1950',
		      u'nicholas-roerich': u'nicholas-roerich_mongolia-campaign-of-genghis-khan',
		      u'pablo-picasso': u'weeping-woman-1937',
		      u'paul-cezanne': u'still-life-with-apples-1894.jpg!HD',
		      u'paul-gauguin': u'Gauguin-the-seed-of-the-areoi-1892',
		      u'samuel-peploe': u'peploe-ile-de-brehat-1911-1',
		      u'vincent-van-gogh': u'vincent-van-gogh_road-with-cypresses-1890',
		      u'wassily-kandinsky': u'Kandinsky-improvisation-28-second-version-1912'}

res_dataset_list = [
    '/data/jsy/code/adaptive-style-transfer/models/model_cezanne/inference_ckpt105000_sz768_for_fid',
    '/data/jsy/code/adaptive-style-transfer/models/model_roerich/inference_ckpt135000_sz768_for_fid',
    '/data/jsy/code/adaptive-style-transfer/models/model_monet/inference_ckpt150000_sz768_for_fid',
    '/data/jsy/code/adaptive-style-transfer/models/model_van-gogh/inference_ckpt300000_sz768_for_fid',
    '/data/jsy/code/adaptive-style-transfer/models/model_picasso/inference_ckpt300000_sz768_for_fid',
    '/data/jsy/code/adaptive-style-transfer/models/model_munch/inference_ckpt90000_sz768_for_fid',
    '/data/jsy/code/adaptive-style-transfer/models/model_peploe/inference_ckpt120000_sz768_for_fid',
    '/data/jsy/code/adaptive-style-transfer/models/model_kandinsky/inference_ckpt150000_sz768_for_fid',
    '/data/jsy/code/adaptive-style-transfer/models/model_kirchner/inference_ckpt90000_sz768_for_fid',
    '/data/jsy/code/adaptive-style-transfer/models/model_morisot/inference_ckpt135000_sz768_for_fid',
    '/data/jsy/code/adaptive-style-transfer/models/model_pollock/inference_ckpt300000_sz768_for_fid',
]

artist_name_list = [
    'paul-cezanne',
    'nicholas-roerich',
    'claude-monet',
    'vincent-van-gogh',
    'pablo-picasso',
    'edvard-munch',
    'samuel-peploe',
    'wassily-kandinsky', #
    'ernst-ludwig-kirchner',
    'berthe-morisot',
    'jackson-pollock',
]

out_dir = 'results/used_for_deception_rate_1'
os.makedirs(out_dir, exist_ok=True)

for i in range(len(artist_name_list)):
    artist_name = artist_name_list[i]
    img_dir = res_dataset_list[i]
    img_name_list = os.listdir(img_dir)
    for img_name in img_name_list:
        ori_img_path = os.path.join(img_dir, img_name)
        img_basename = os.path.splitext(img_name)[0]
        dst_path = os.path.join(out_dir, f'{img_basename}_{artist_name}.jpg')
        shutil.copy(ori_img_path, dst_path)
        print(f'copy [{ori_img_path}] to [{dst_path}]')
