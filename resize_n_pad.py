import os
import numpy as np
import os
import PIL
from PIL import Image
from multiprocessing import Pool

def pad_image(img_path, output_path, target_size, pad_size=[8, 8, 8, 8]):
    """Pads image with pad size

    Args:
        img_path: (string) path to image
        output_path: (string) path to output image
        target_size: [width, height] 统一的大小
        pad_size: list of 4 ints

    """
    top, left, bottom, right = pad_size
    old_im = Image.open(img_path)
    #resize
    im = old_im.resize((target_size[0], target_size[1]), Image.ANTIALIAS)
    _size = (im.size[0] + left + right, im.size[1] + top + bottom)
    new_im = Image.new("RGB", _size, (255, 255, 255))
    new_im.paste(im, (left, top))
    new_im.save(output_path)

input_image_dir = '../datasets_no_test/train/img/'
output_image_dir = '../datasets_no_test/train/pad_img/'
if not os.path.isdir(output_image_dir):
    os.mkdir(output_image_dir)

img_path_list = os.listdir(input_image_dir)

target_w, target_h = 0, 0
for img_path in img_path_list:
    im = Image.open(input_image_dir + img_path)
    target_w = max(target_w, im.size[0])
    target_h = max(target_h, im.size[1])
print(target_w, target_h)

# for img_path in img_path_list:
#     # pad_image(input_image_dir + img_path, output_image_dir + os.path.basename(img_path), buckets=buckets)
#     pad_image(input_image_dir + img_path, output_image_dir + os.path.basename(img_path), [target_w, target_h])