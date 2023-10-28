import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

def GPU(img,out):
    image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

    image_gpu = cv2.cuda_GpuMat()
    image_gpu.upload(image)

    img_lab = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
    l, a, b = cv2.split(img_lab)

    clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(2, 2))
    l_corrected = clahe.apply(l)
    img_lab_corrected = cv2.merge((l_corrected, a, b))
    img_corrected = cv2.cvtColor(img_lab_corrected, cv2.COLOR_Lab2BGR)

    result_gpu = cv2.cuda_GpuMat()
    result_gpu.download(result_image)
    return  result_gpu

def apply_gamma_correction(image, gamma=1.0):
    corrected_image = np.power(image, gamma)
    corrected_image = np.uint8(255 * (corrected_image / np.max(corrected_image)))
    return corrected_image

# 自适应直方图均衡化（AHE）
def apply_adaptive_histogram_equalization(image, clip_limit=2.0):
    clahe = cv2.createCLAHE(clipLimit=clip_limit)
    enhanced_image = clahe.apply(image)
    return enhanced_image

# 对比度受限的自适应直方图均衡化（CLAHE）
def apply_contrast_limited_adaptive_histogram_equalization(image, clip_limit=2.0):
    clahe = cv2.createCLAHE(clipLimit=clip_limit)
    enhanced_image = clahe.apply(image)
    return enhanced_image

# 多尺度对比度增强（MSRCR）
def apply_multiscale_retinex(image, sigma_list=(15, 80, 250)):
    msrcr_image = np.zeros_like(image, dtype=np.float32)
    for sigma in sigma_list:
        retinex = np.log(image + 1) - np.log(cv2.GaussianBlur(image, (0, 0), sigma) + 1)
        msrcr_image += retinex
    msrcr_image = (msrcr_image / len(sigma_list)) * 255
    return np.uint8(msrcr_image)

def apply_gamma_correction(img, gamma):
    inv_gamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(img, table)


def apply_clahe_and_gamma_correction(image_path, gamma_value=1.2):
    img = cv2.imdecode(np.fromfile(image_path, dtype=np.uint8), 1)
    img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
    l, a, b = cv2.split(img_lab)
    clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(2, 2))
    l_corrected = clahe.apply(l)
    img_lab_corrected = cv2.merge((l_corrected, a, b))
    img_corrected = cv2.cvtColor(img_lab_corrected, cv2.COLOR_Lab2BGR)
    img_hsv = cv2.cvtColor(img_corrected, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(img_hsv)
    v_corrected = apply_gamma_correction(v, gamma_value)
    img_hsv_corrected = cv2.merge((h, s, v_corrected))
    img_corrected = cv2.cvtColor(img_hsv_corrected, cv2.COLOR_HSV2BGR)
    return img_corrected


if __name__ == '__main__':

    input_image = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)
    image_path = 'D:/OSNET/Yolov7_OC_SORT/sci-clahe/experience/5.png'
    gamma_value = 1.2
    corrected_image = apply_clahe_and_gamma_correction(image_path, gamma_value)
    gamma_corrected = apply_gamma_correction(input_image, gamma=2.0)