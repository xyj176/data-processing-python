#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：data-processing-python 
@File    ：converter.py
@IDE     ：PyCharm 
@Author  ：xuyj
@Date    ：2024/6/21 15:28 
"""
import os.path
from pathlib import Path

from osgeo import gdal
import numpy as np
from PIL import Image


def convert(tif, save_dir):
    """

    Args:
        tif (): 4波段16bit的tif影像
        save_dir (): 结果保存路径

    Returns:

    """
    data = gdal.Open(tif)  # 读取tif文件
    num_bands = data.RasterCount  # 获取波段数
    print(num_bands)
    tmp_img = data.ReadAsArray()  # 将数据转为数组
    img_rgb_16bit = tmp_img.transpose(1, 2, 0)  # 矩阵转置：由波段、行、列——>行、列、波段

    img_rgb_16bit = np.array(img_rgb_16bit)
    min_16bit = np.min(img_rgb_16bit)
    max_16bit = np.max(img_rgb_16bit)

    # 线性转换为8bit
    r_8bit = np.array((img_rgb_16bit[:, :, 2] - min_16bit) / float(max_16bit - min_16bit) * 255.0, dtype=np.uint8)
    g_8bit = np.array((img_rgb_16bit[:, :, 1] - min_16bit) / float(max_16bit - min_16bit) * 255.0, dtype=np.uint8)
    b_8bit = np.array((img_rgb_16bit[:, :, 0] - min_16bit) / float(max_16bit - min_16bit) * 255.0, dtype=np.uint8)
    img_rgb_8bit = np.dstack((r_8bit, g_8bit, b_8bit))  # 波段组合
    img = Image.fromarray(img_rgb_8bit)

    # 结果保存到本地
    tif_8bit = Path(tif).stem + ".tif"
    img.save(os.path.join(save_dir, tif_8bit), "TIFF")


def method():
    tif_root_dir_16bit = r"D:\data\open-data\cd\Hi-CNA dataset\train\image2"
    tif_root_dir_8bit = r"D:\data\open-data\cd\Hi-CNA dataset\sm_train\Images2"
    for item in os.listdir(tif_root_dir_16bit):
        tif_16bit = os.path.join(tif_root_dir_16bit, item)
        convert(tif_16bit, tif_root_dir_8bit)


if __name__ == "__main__":
    method()
    print("OK")
