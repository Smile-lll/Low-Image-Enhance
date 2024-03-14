
from skimage.metrics import mean_squared_error as mse
from PIL import Image
import numpy as np
import os



if __name__ == "__main__":
    # 获取文件夹中的所有图像文件
    image_files = [f for f in os.listdir('../enhanced') if f.endswith(('.png', '.jpg', '.jpeg'))]
    # print(image_files)
    img=[]
    lst_mse=[]
    img.append(np.array(Image.open('../rsc/1.png')))
    i=1
    with open('mse.txt','w') as f:
        for image_file in image_files:
            img.append(np.array(Image.open('../enhanced/'+image_file)))
            lst_mse.append(mse(img[0],img[i]))
            print(f'{image_file}的MSE值(越小越好):', lst_mse[i-1])
            f.write(str(lst_mse[i-1]) + '\n')
            i+=1



