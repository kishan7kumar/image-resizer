import cv2

# Configuration
src = "big-image.jpg"
destination = "resize.jpg"
scale_percent = 40

image = cv2.imread(src, cv2.IMREAD_UNCHANGED)
cv2.imshow("title", image)

width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)

output = cv2.resize(image, (width, height))
cv2.imwrite(destination, output)

cv2.waitKey(0)
