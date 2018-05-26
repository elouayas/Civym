import numpy as np
import matplotlib.pyplot as plt
import cv2
def average_square(image, x,y, square_size):
    square_size = square_size//2
    if x < square_size or y < square_size or x > x_length - square_size or y > x_length - square_size :
        return image[x,y]
    val = 0
    x_init = x - square_size
    y_init = y - square_size
    number = 0
    for i in range(square_size):
        for j in range(square_size):        
            val = val + image[x_init+i,y_init+j] + image[x_init+2*i+1,y_init+2*i+1]
            number += 2
    return val/number
def pixel():
    a, b, c = pixel
    return (a+b+c)/3

def blur(image, square_size=15):
    matrix = np.zeros([x_length,y_length])
    for x in range(0, x_length, step):
        for y in range(0, y_length, step):
            av = average_square(image, x, y, square_size)
            matrix[x,y] = av
    return matrix
image = cv2.imread("thresh = 62.png", 0)
x_length = image.shape[0]
y_length = image.shape[1]
step = 10
cv2.imwrite("testblurred.jpg", blur(image))

