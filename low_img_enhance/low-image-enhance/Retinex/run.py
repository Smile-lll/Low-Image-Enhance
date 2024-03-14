
import os

import cv2
import json

import retinex


data_path = '../rsc'
img_list = os.listdir(data_path)
print(img_list)
if len(img_list) == 0:
    print('Data directory is empty.')
    exit()

with open('../config.json', 'r') as f:
    config = json.load(f)
    # print(config['sigma_list'][0])
for img_name in img_list:
    if img_name == '.gitkeep':
        continue

    img = cv2.imread(os.path.join(data_path, img_name))

    img_msrcr = retinex.MSRCR(
        img,
        config['sigma_list'],
        config['G'],
        config['b'],
        config['alpha'],
        config['beta'],
        config['low_clip'],
        config['high_clip']
    )

    img_amsrcr = retinex.automatedMSRCR(
        img,
        config['sigma_list']
    )

    img_msrcp = retinex.MSRCP(
        img,
        config['sigma_list'],
        config['low_clip'],
        config['high_clip']
    )
    shape = img.shape
    print(shape)
    # cv2.imshow('Image', img)
    # cv2.imshow('MSRCR', img_msrcr)
    cv2.imwrite('../enhanced/MSRCR.png', img_msrcr)
    # cv2.imshow('Automated MSRCR', img_amsrcr)
    cv2.imwrite('../enhanced/Automated MSRCR.png', img_amsrcr)
    # cv2.imshow('MSRCP', img_msrcp)
    cv2.imwrite('../enhanced/MSRCP.png', img_msrcp)

    # cv2.imshow('Image', img)
    # enhanced_list = os.listdir('./enhanced/')
    # if len(enhanced_list) == 0:
    #     print('Data directory is empty.')
    #     exit()
    # for enhanced_img in enhanced_list:
    #     img_show=cv2.imread(f'./enhanced/{enhanced_img}')
    #     cv2.imshow(f'{enhanced_img}', img_show)
    # cv2.waitKey()
