import cv2
src = cv2.imread("image.jpg", cv2.IMREAD_UNCHANGED)
scale_percent = 50
# calculate the 50 percent of original dimensions
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)
dsize = (width, height)
output = cv2.resize(src, dsize)
cv2.imwrite("image.jpg", output)
cv2.waitKey(0)


