import os
import argparse


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
    import cv2
    img = cv2.imread('example.jpg')  # 图片不支持中文名
    print(img.shape)  # shape：高，宽，通道
    crop = img[0:2000, 0:2000]  # 裁剪坐标为[y0:y1, x0:x1],图片左上角为原点
    cv2.imwrite('crop_cv2.jpg', crop)


def clip_pil_example():
    """
    通过PIL裁剪图片的示例代码
    :return:
    """
    from PIL import Image
    img = Image.open('example.jpg')
    print(img.size)  # size:宽，高
    crop = img.crop((0, 0, 2000, 2000))  # (left, upper, right, lower)
    crop.save('crop_pil.jpg')


def clip_cv2(img_path: str):
    import cv2
    img = cv2.imread(img_path)
    pass


def clip_pil(img_path: str):
    from PIL import Image
    img = Image.open(img_path)

    pass


def main():
    args = parse_args()
    data_root = args.data_root

    pass


if __name__ == '__main__':
    # clip_pil_example()
    clip_cv2_example()
    # main()
