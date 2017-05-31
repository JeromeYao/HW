import cv2
import numpy as np
from matplotlib import pyplot as plt

'''
使用如下测试代码，用于同时显示原始图片和快速傅里叶变换后的结果。
同目录下需存有apple.jpe文件
'''
img = cv2.imread('apple.jpg', 0)
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

magnitude_spectrum = 20 * \
    np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
plt.subplot(121).imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122).imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.savefig('a.png', format='png')
plt.show()
