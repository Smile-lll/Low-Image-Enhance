import argparse
from argparse import RawTextHelpFormatter
import glob
from os import makedirs
from os.path import join, exists, basename, splitext

import cv2
from tqdm import tqdm

from exposure_enhancement import enhance_image_exposure


def main(args):
    # 导入图片
    imdir = args.folder
    print(imdir)
    ext = ['png', 'jpg', '.jpeg']  # Add image formats here
    files = []
    [files.extend(glob.glob(imdir + '*.' + e)) for e in ext]
    # print(files)
    images = [cv2.imread(file) for file in files]

    # 指定保存位置
    directory = '../enhanced/'
    if not exists(directory):
        makedirs(directory)

    # 增强低照度图片
    for i, image in tqdm(enumerate(images), desc="运行中"):
        enhanced_image = enhance_image_exposure(image, args.gamma, args.lambda_, not args.lime,
                                                sigma=args.sigma, bc=args.bc, bs=args.bs, be=args.be, eps=args.eps)
        filename = basename(files[i])#glob.glob返回绝对路径 由basename取文件名
        name, ext = splitext(filename)
        # print(ext)带.
        method = "LIME" if args.lime else "DUAL"
        # enhanced_name = f"{method}_G{args.gamma}_L{args.lambda_}{ext}"
        enhanced_name = f"{method}{ext}"
        cv2.imwrite(join(directory, enhanced_name), enhanced_image)

        # img_show = cv2.imread(f'../enhanced/{enhanced_name}')
        # cv2.imshow(f'{enhanced_name}', img_show)
        # cv2.waitKey()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="通过光照图估算实现两种弱光图像增强技术的 Python 实现(LIME).",
        formatter_class=RawTextHelpFormatter
    )
    parser.add_argument("-f", '--folder', default='../rsc/', type=str,
                        help="folder path to test images.")
    parser.add_argument("-g", '--gamma', default=0.6, type=float,
                        help="the gamma correction parameter.")
    parser.add_argument("-l", '--lambda_', default=0.15, type=float,
                        help="the weight for balancing the two terms in the illumination refinement optimization objective.")
    parser.add_argument("-ul", "--lime", default=True, action="store_true",
                        help="Use the LIME method. By default, the DUAL method is used.")
    parser.add_argument("-s", '--sigma', default=3, type=int,
                        help="Spatial standard deviation for spatial affinity based Gaussian weights.")
    parser.add_argument("-bc", default=1, type=float,
                        help="parameter for controlling the influence of Mertens's contrast measure.")  # 对比度
    parser.add_argument("-bs", default=1, type=float,
                        help="parameter for controlling the influence of Mertens's saturation measure.")  # 饱和度
    parser.add_argument("-be", default=1, type=float,
                        help="parameter for controlling the influence of Mertens's well exposedness measure.")  # 曝光度
    parser.add_argument("-eps", default=1e-3, type=float,
                        help="constant to avoid computation instability.")

    args = parser.parse_args()  # 解析参数
    main(args)
