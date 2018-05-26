import numpy as np
import matplotlib.pyplot as plt
import cv2
#def average_square(image, x,y, square_size):
#   square_size = square_size//2
#   if x < 2 or y < 2 or x > x_length - 2 or y > y_length - 2#
#       return image[x,y] 
#   else :
#       val = int(image[x-1,y-1])+ int(image[x,y-1]) + int(image[x+1, y-1])
#       val += int(image[x-1,y])+ int(image[x,y])+ int(image[x+1, y])
#       val += int(image[x-1,y+1]) + int(image[x,y+1]) + int(image[x+1,y+1])
#       val = val // 9
#       return val

#def blur(image, square_size=15):
#   matrix = np.zeros([x_length,y_length])
#   for x in range(0, x_length):
#      for y in range(0, y_length):
#           av = average_square(image, x, y, square_size)
#           matrix[x,y] = av 
#   return matrix
#s_plan = cv2.imread("croppedplan.png",0)
number = 72
#_length = image.shape[0]
#_length = image.shape[1]
#tep = 4
#ize = 5 
#v2.imwrite("blurred{}.jpg".format(number), blur(image, size))



image = cv2.imread("double_convo.jpg")
greyscale_plan = cv2.imread("greyscale_plan.jpg")
initial_layer = cv2.imread("thresh{}.jpg".format(number),0)
convo = initial_layer
ks = 30
kernel = 3*np.ones((ks,ks), np.float32)/(ks*ks)
seuil = cv2
firstconvo = cv2.filter2D(initial_layer, -1, kernel)
double_convo = cv2.filter2D(firstconvo, -1, kernel)
white = np.zeros(image.shape)
cv2.imwrite('secondtest.jpg', double_convo)
second_test_gs = cv2.imread('secondtest.jpg',0)
nlayer = 5
max_bright = 0
for x_index, x_elt in enumerate(greyscale_plan):
    for y_index, y_elt in enumerate(x_elt):
        B, G, R = y_elt
        brightness = second_test_gs[x_index, y_index]
        if brightness > max_bright :
            max_bright = brightness
        if brightness < 85 : 
            greyscale_plan[x_index,y_index] =  [0,0,int(brightness*G)]
        elif brightness < 170:
            greyscale_plan[x_index,y_index] = [0,int(brightness*G),int(brightness*G)]
        else : 
            greyscale_plan[x_index,y_index] =  [0,int(brightness*G),0 ]


print(max_bright)
cv2.imwrite("final.jpg",greyscale_plan)


 










#for layer in range(nlayer):
#   convo_buffer = convo
#   convo = cv2.filter2D(initial_layer,-1, kernel)
#   initial_layer = convo
#cv2.imwrite("{}convo.jpg".format(nlayer),convo)

