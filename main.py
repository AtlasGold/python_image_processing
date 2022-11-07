import cv2
import numpy as np

img = cv2.imread('meteor_challenge_01.png')

# Modify image colors (i found it easier to deal with them in that color)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)


# Save the modified image 
cv2.imwrite('inverted_img.png',hsv)

# Blue scale range
BLUE_MIN = np.array([0, 0, 200], np.uint8)
BLUE_MAX = np.array([50, 50, 255], np.uint8)

# White scale range
WHITE_MIN = np.array([250, 250, 250], np.uint8)
WHITE_MAX = np.array([255, 255, 255], np.uint8)

# Identifies white and blue pixels
dst_blue = cv2.inRange(img, BLUE_MIN, BLUE_MAX)
dst_white = cv2.inRange(img, WHITE_MIN,WHITE_MAX)

# Counts the number of pixels by color
n_blue = cv2.countNonZero(dst_blue)
n_white= cv2.countNonZero(dst_white)

print('The number of meteors is: ' + str(n_blue))
print('The number of stars is: ' + str(n_white))


inverted_img = cv2.imread('inverted_img.png')

# Make a True/False mask of blue pixels and save for debug
blue = np.all(inverted_img==[255,0,0], axis=2)
cv2.imwrite('DEBUG-blue.png', blue*255)

# Make a True/False mask of red pixels and save for debug
red = np.all(inverted_img==[0,0,255], axis=2)
cv2.imwrite('DEBUG-red.png', red*255)

# Make a True/False mask of white pixels and save for debug
white = np.all(inverted_img==[255,255,255], axis=2)
cv2.imwrite('DEBUG-white.png', white*255)

# Get all columns with red pixels in them
colsWithRed = np.argwhere(np.any(red==True, axis=0))

# Get all columns with blue pixels in them
colsWithBlue = np.argwhere(np.any(blue==True, axis=0))

# Get all columns with red and blue
both = np.intersect1d(colsWithBlue,colsWithRed)
print(f'The number of meteors that will fall into the water: {len(both)}')


cv2.imshow('Image',hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()