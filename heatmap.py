import numpy as np
import cv2
import matplotlib.pyplot as plt


def CenterLabelHeatMap(img_width, img_height, c_x, c_y, sigma):
    X1 = np.linspace(1, img_width, img_width)
    Y1 = np.linspace(1, img_height, img_height)
    [X, Y] = np.meshgrid(X1, Y1)
    X = X - c_x
    Y = Y - c_y
    D2 = X * X + Y * Y
    E2 = 2.0 * sigma * sigma
    Exponent = D2 / E2
    heatmap = np.exp(-Exponent)
    return heatmap

image_file = 'heat.png'
img = cv2.imread(image_file)

height, width,_ = np.shape(img)
cy, cx = height*4.0/7.0, width*1.0/8.0

heatmap1 = CenterLabelHeatMap(width, height, cx, cy, 21)

plt.imshow(heatmap1)
plt.show()
