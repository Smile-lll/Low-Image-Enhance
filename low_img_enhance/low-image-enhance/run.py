import LIME as lime
import Retinex as retinex
import cv2
import os
if __name__ == '__main__':
    retinex = retinex
    lime = lime

    data_path = './rsc'
    img_list = os.listdir(data_path)
    # print(img_list)
    if len(img_list) == 0:
        print('Data directory is empty.')
        exit()
    for img_name in img_list:
        if img_name == '.gitkeep':
            continue

        img = cv2.imread(os.path.join(data_path, img_name))

        cv2.imshow('Image', img)
        enhanced_list = os.listdir('./enhanced/')
        if len(enhanced_list) == 0:
            print('Data directory is empty.')
            exit()
        for enhanced_img in enhanced_list:
            img_show=cv2.imread(f'./enhanced/{enhanced_img}')
            cv2.imshow(f'{enhanced_img}', img_show)
        cv2.waitKey()