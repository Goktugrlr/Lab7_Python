import cv2

image = cv2.imread('lion.jpg')
height, width = image.shape[:2]
image = cv2.resize(image, (int(width*1.5), int(height*1.5)))

B, G, R = cv2.split(image)

sortedChannels = cv2.hconcat([B, G, R])
cv2.imshow('Blue - Green - Red (respectively)', sortedChannels)

g = G * 0

withoutGreen = cv2.merge([B, g, R])
cv2.imshow('Blue + Red', withoutGreen)

originalVersion = cv2.merge([B, G, R])
cv2.imshow('Original', originalVersion)
cv2.waitKey(0)
cv2.destroyAllWindows()
