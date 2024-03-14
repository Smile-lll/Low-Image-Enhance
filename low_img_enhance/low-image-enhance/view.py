from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker
import os

path = 'enhanced'
# 获取文件夹中的所有图像文件
image_files = [f for f in os.listdir(path) if f.endswith(('.png', '.jpg', '.jpeg'))]
with open('./index/niqe.txt', 'r') as f:
    lst_niqe = f.readlines()
    print(lst_niqe, image_files)
    for i in range(len(lst_niqe)):
        lst_niqe[i] = lst_niqe[i][:-1]
with open('./index/psnr.txt', 'r') as f:
    lst_psnr = f.readlines()
    print(lst_psnr, image_files)
    for i in range(len(lst_psnr)):
        lst_psnr[i] = lst_psnr[i][:-1]
with open('./index/ssim.txt', 'r') as f:
    lst_ssim = f.readlines()
    print(lst_ssim, image_files)
    for i in range(len(lst_ssim)):
        lst_ssim[i] = lst_ssim[i][:-1]
with open('./index/mse.txt', 'r') as f:
    lst_mse = f.readlines()
    print(lst_mse, image_files)
    for i in range(len(lst_mse)):
        lst_mse[i] = lst_mse[i][:-1]

c = (
    Bar()
    .add_xaxis(['AutoMSRCR', 'DUAL','LIME', 'MSRCP', 'MSRCR','RetinexNet'])
    # .add_yaxis("SSIM",lst_ssim,bar_width=60)
    # .add_yaxis("MSE",lst_mse,bar_width=60)

    .add_yaxis("PSNR", lst_psnr)
    # .add_yaxis("SSIM", lst_ssim)
    .add_yaxis("NIQE", lst_niqe)
    # .add_yaxis("MSE", lst_mse)
    .set_global_opts(title_opts=opts.TitleOpts(title="各项指标", subtitle="指标数值"))
    .render("bar_index.html")
)
