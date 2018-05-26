import numpy as np
import matplotlib.pyplot as plt
import cv2
def average_square(image, x,y, square_size):
    square_size = square_size//2
    if x < 2 or y < 2 or x > x_length - 2 or y > y_length - 2:
        return image[x,y] #il faudra améliorer cette imprécision
    else :
        val = int(image[x-1,y-1])+ int(image[x,y-1]) + int(image[x+1, y-1])
        val += int(image[x-1,y])+ int(image[x,y])+ int(image[x+1, y])
        val += int(image[x-1,y+1]) + int(image[x,y+1]) + int(image[x+1,y+1])
        val = val // 9
        return val

def blur(image, square_size=15):
    matrix = np.zeros([x_length,y_length])
    for x in range(0, x_length):
        for y in range(0, y_length):
            av = average_square(image, x, y, square_size)
            matrix[x,y] = av 
    return matrix
number = 72
plan = cv2.imread("croppedplan.png")
print(plan.shape)
x_length = image.shape[0]
y_length = image.shape[1]
step = 4
size = 5 
kernel = np.ones((40,40), np.float32)/1600
firstconvo = cv2.filter2D(image, -1, kernel)
       
cv2.imwrite("blurred{}.jpg".format(number), blur(image, size))

initial_layer = cv2.imread("thresh{}.jpg".format(number),0)
gs_plan = cv2.imread("croppedplan.png",0)
cv2.imwrite("greyscale_plan.jpg",gs_plan)
greyscale_plan = cv2.imread("greyscale_plan.jpg")
convo = initial_layer
nlayer = 5
double_convo = cv2.filter2D(firstconvo, -1, kernel)
grey = np.zeros(image.shape)
for x_index, x_elt in enumerate(greyscale_plan):
    for y_index, y_elt in enumerate(x_elt):
        B, G, R = y_elt
        greyscale_plan[x_index,y_index] =  [128, 128  + int(double_convo[x_index, y_index]), 128]
cv2.imwrite("final.jpg",greyscale_plan)
 










for layer in range(nlayer):
    convo_buffer = convo
    convo = cv2.filter2D(initial_layer,-1, kernel)
    initial_layer = convo
cv2.imwrite("{}convo.jpg".format(nlayer),convo)

