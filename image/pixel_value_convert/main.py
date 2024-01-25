import cv2


def convert(img_path: str, src: int, dst: int):
    """
    像素值转换：255→1
    :param img_path: 图片路径
    :param src: 源像素值
    :param dst: 目标像素值
    :return: 原图将会被重新覆盖
    """
    img = cv2.imread(img_path)
    img[img == src] = dst
    cv2.imwrite(img_path, img)


if __name__ == '__main__':
    img_path = '3.tif'
    convert(img_path, 255, 1)
    print('OK')
