import os
import argparse
import cv2
from PIL import Image


def parse_args():
    parser = argparse.ArgumentParser(description="影像数据裁剪处理")
    parser.add_argument('data_root', help='影像数据的根目录')
    args = parser.parse_args()
    return args


def clip_cv2_example():
    """
    通过cv2裁剪图片的示例代码
    :return:
    """
    img = cv2.imread('example.jpg')  # cv2不支持中文路径，读写都不支持
    print(img.shape)  # shape：高，宽，通道
    crop = img[0:2000, 0:2000]  # 裁剪坐标为[y0:y1, x0:x1],图片左上角为原点
    cv2.imwrite('crop_cv2.jpg', crop)


def clip_pil_example():
    """
    通过PIL裁剪图片的示例代码
    :return:
    """
    img = Image.open('example.jpg')
    print(img.size)  # size:宽，高
    crop = img.crop((0, 0, 2000, 2000))  # (left, upper, right, lower)
    crop.save('crop_pil.jpg')


def clip(img_path, out_path, size_w=512, size_h=512, step=512):
    """
    将图片按照指定的尺寸进行裁剪，并对边缘处不满足尺寸大小的部分进行特殊处理
    :param img_path: 源图片
    :param out_path: 裁剪后输出的路径
    :param size_w: 裁剪的宽，默认512
    :param size_h: 裁剪的高，默认512
    :param step: 滑动裁剪的步长，如果步长小于裁剪的尺寸则会出现重叠，默认512
    :return:
    """
    base_name = os.path.basename(img_path)
    name, suffix = os.path.splitext(base_name)  # 后缀
    img = cv2.imread(img_path)
    height = img.shape[0]
    width = img.shape[1]

    for h in range(0, height, step):
        star_h = h
        end_h = star_h + size_h
        if end_h > height:  # 如果边缘位置不够512的行，以最后一行开始倒数512行
            star_h = height - size_h
            end_h = star_h + size_h
        for w in range(0, width, step):
            star_w = w
            end_w = star_w + size_w
            if end_w > width:  # 如果边缘位置不够512的列，以最后一列开始倒数512列
                star_w = width - size_w
                end_w = star_w + size_w
            crop = img[star_h:end_h, star_w:end_w]
            dst_name = name + '_' + str(star_h) + '_' + str(star_w) + suffix  # 用起始点的y,x坐标命名
            print(dst_name)
            cv2.imwrite(os.path.join(out_path, dst_name), crop)


def clip_batch(data_root, out_path, size_w, size_h, step):
    for item in os.listdir(data_root):
        src_img = os.path.join(data_root, item)
        clip(src_img, out_path)


def main():
    args = parse_args()
    data_root = args.data_root
    pass


if __name__ == '__main__':
    data_root = r'D:\code\data-processing-python\image\clip\data\Masks'
    out_path = r'D:\code\data-processing-python\image\clip\result\Masks'
    clip_batch(data_root, out_path, 512, 512, 512)
    # main()
